from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import os
from django.core.files.base import ContentFile
from django.conf import settings
from images.serializers.images import ImagesSerializer
from images.models.images import Images
from PIL import Image as PILImage
import base64
from io import BytesIO

class ImagesView(APIView):

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        image_name = request.data.get('name')
        image_base64 = request.data.get('image')


        if not all([user_id, image_name, image_base64]):
            return Response({"detail": "Faltam dados obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        if Images.objects.filter(name=image_name).exists():
           return Response({"detail": "Imagem já existe no banco de dados."}, status=status.HTTP_409_CONFLICT)

        path = os.path.join('/media/images', image_name)

        try:
            image_data = base64.b64decode(image_base64.split(',')[1])
            image = PILImage.open(BytesIO(image_data))
            
            os.makedirs(os.path.dirname(path), exist_ok=True)
            image.save(path)

        except Exception as ex:
            print(ex)
            return Response({"detail": "Erro ao salvar a imagem."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ImagesSerializer(data={'name': image_name, 'path': path, 'user': user_id})

        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Imagem processada e salva com sucesso!", "path": path}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
