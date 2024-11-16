from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import os
import base64
from io import BytesIO
from PIL import Image as PILImage
from images.serializers.images import ImagesSerializer
from results.serializers.results import ResultsSerializer
from images.models.images import Images
from process_images.process_images import ProcessImages

class ImagesView(APIView):
    def _convert_pil_to_base64(self, pil_image):
        format='jpeg'
        buffer = BytesIO()
        pil_image.save(buffer, format=format)
        image_binary = buffer.getvalue()
        image_base64 = base64.b64encode(image_binary).decode('utf-8')
        return f"data:image/{format};base64,{image_base64}"

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        image_name = request.data.get('name')
        image_base64 = request.data.get('image')
        output_path = '/media/images'

        if not all([user_id, image_name, image_base64]):
            return Response({"detail": "Faltam dados obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        if Images.objects.filter(name=image_name).exists():
           return Response({"detail": "Imagem já existe no banco de dados."}, status=status.HTTP_409_CONFLICT)

        path = os.path.join(output_path, image_name)

        try:
            image_data = base64.b64decode(image_base64.split(',')[1])
            image = PILImage.open(BytesIO(image_data))
            
            os.makedirs(os.path.dirname(path), exist_ok=True)
            image.save(path)

        except Exception as ex:
            print(ex)
            return Response({"detail": "Erro ao salvar a imagem."}, status=status.HTTP_400_BAD_REQUEST)

        imagesSerializer = ImagesSerializer(data={'name': image_name, 'path': path, 'user': user_id})

        current_dir = os.path.dirname(os.path.abspath(__file__))
        yolo_model_path = f'{current_dir}/../../yolo-model/yolo-model.pt'
        print(yolo_model_path)
        process = ProcessImages(yolo_model_path, output_path, ['placa-carro'])

        img_data_processed, img_path, img_classes_data = process.detect_image_classes(image, image_name)
        number_of_plates = len(img_classes_data)

        plate = [{'text': item.plate, 'confidence': item.plate_confidence} for item in img_classes_data]

        image_base64_processsed = self._convert_pil_to_base64(img_data_processed)

        if imagesSerializer.is_valid():
            image_saved = imagesSerializer.save()
            for item in img_classes_data:
                resultsSerializer = ResultsSerializer(data={
                    'user': user_id,
                    'image': image_saved.id,
                    'x_min': item.x1,
                    'y_min': item.y1,
                    'x_max': item.x2,
                    'y_max': item.y2,
                    'points_precision': item.plate_confidence,
                    'license_plate': item.plate,
                    'plate_precision': item.plate_confidence})
                if resultsSerializer.is_valid():
                    print(' result eh valido ')
                    resultsSerializer.save()

            return Response({
                "detail": "Imagem processada e salva com sucesso!",
                "path": img_path, "image": image_base64_processsed,
                "number_of_plates": number_of_plates, "plate": plate},
                status=status.HTTP_201_CREATED)
        else:
            return Response(imagesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
