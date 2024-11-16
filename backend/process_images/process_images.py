from ultralytics import YOLO
import cv2
from PIL import Image
import random
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Tuple, List
from dataclasses import dataclass

from process_images.plate_text_extractor import PlateTextExtractor
from process_images.save_file import SaveFile


@dataclass
class ProcessImageData:
    x1: int
    y1: int
    x2: int
    y2: int
    class_id: int
    class_name: str
    class_confidence: float
    plate: str
    plate_confidence: float
    roi_path: str


class ProcessImages:
    def __init__(self, yolo_model_path, output_path, classes_list, confidence_threshold=0.2):
        self.plate_text = PlateTextExtractor()
        self.save_file = SaveFile()
        self.yolo_model = YOLO(yolo_model_path)

        self.confidence_threshold = confidence_threshold
        self.enabled_class_list = classes_list
        self.output_path = output_path

        print(f"Classes enabled: {self.enabled_class_list} - classes mapped: {self.yolo_model.names}")

    def _get_box_data(self, box) -> Tuple[int, int, int, int, float, int, str]:
        x1, y1, x2, y2, confidence, class_id = box
        x1, y1, x2, y2, class_id = map(int, (x1, y1, x2, y2, class_id))
        confidence = float(confidence)
        class_name = self.yolo_model.names[class_id]
        return x1, y1, x2, y2, confidence, class_id, class_name

    def _save_processed_img(self, image_name, image, number_of_classes) -> str:
        croped_image_name = (
            f"{image_name}_processed.jpg"
        )
        ret = self.save_file.save_image(self.output_path, croped_image_name, image)
        return ret

    def _save_roi_img(
        self, index, image_name, roi, class_name, class_score, text, text_confidence
    ) -> str:
        date_fmt = datetime.now().strftime("%Y%m%d_%H%M%S.%f")
        croped_image_name = f"{image_name}_{class_name}_score{class_score:.4f}_plate_{text}_score{text_confidence:.4f}_{date_fmt}.jpg"
        saved_path = self.save_file.save_image(self.output_path, croped_image_name, roi)
        return saved_path

    def _draw_class_region(
        self, image, x1, y1, x2, y2, class_id, class_name, confidence
    ):
        random.seed(class_id + 100)
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)

        label = f"{class_name}: {confidence*100:.4f}%"
        label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        label_y = max(y1 - 10, label_size[1])

        cv2.rectangle(
            image,
            (x1, label_y - label_size[1] - 5),
            (x1 + label_size[0], label_y + 5),
            color,
            -1,
        )
        cv2.putText(
            image, label, (x1, label_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1
        )

    def read_image_file(self, image_path):
        return cv2.imread(image_path)

    def convert_cv2_to_bytes(self, image_cv2, image_format="jpg") -> bytes:
        # Encode the image to the specified format
        ret, buffer = cv2.imencode(
            f".{image_format}", image_cv2, [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        )
        if not ret:
            print("Image encoding failed")
            return None

        # Convert the buffer to bytes
        image_bytes = buffer.tobytes()
        return image_bytes
    
    def convert_cv2_to_pil(self, image_cv2):
        return Image.fromarray(cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB))

    def convert_bytes_to_cv2_image(self, pil_image: bytes):
        # Convert image PIL to a NumPy array
        cv2_image = np.array(pil_image)

        if pil_image.mode == 'RGB':
            cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_RGB2BGR)
        return cv2_image

    def detect_image_classes(self, image_data, image_name) -> Tuple[bytes, str, List[ProcessImageData]]:

        count_classes = 0
        detected_classes = []

        print('DetectPlate - detect_image_classes() - Starting')

        image = self.convert_bytes_to_cv2_image(image_data)

        processed_image = image.copy()  # Make a copy to edit and apply classes labels

        results = self.yolo_model(image)  # Process image using yolo model

        for index, box in enumerate(results[0].boxes.data):
            x1, y1, x2, y2, confidence, class_id, class_name = self._get_box_data(box)

            print(
                f"Detected '{class_name}' with confidence {confidence:.2f} and location {x1}:{y1}-{x2}:{y2}"
            )

            if (
                len(self.enabled_class_list) > 0
                and class_name not in self.enabled_class_list
            ):
                print(f"Class {class_name} not mapped")
                continue

            if confidence < self.confidence_threshold:
                print(
                    f"Confidence below then the threshould {self.confidence_threshold}: {confidence:.2f}"
                )
                continue

            count_classes += 1
            self._draw_class_region(
                processed_image, x1, y1, x2, y2, class_id, class_name, confidence
            )

            # Extract the Region Of Interest (ROI) from the original image
            roi = image[y1:y2, x1:x2]
            text, text_confidence = self.plate_text.extract_plate_text(roi)
            print(f"Extracted text {text} with confidence {text_confidence:0.4f}")

            # Save ROI in the output dir
            roi_path = self._save_roi_img(
                index,
                Path(image_name).name,
                roi,
                class_name,
                confidence,
                text,
                text_confidence,
            )

            # Get class info to return after image processing
            detected_classes.append(
                ProcessImageData(
                    x1=x1,
                    x2=x2,
                    y1=y1,
                    y2=y2,
                    class_id=class_id,
                    class_name=class_name,
                    class_confidence=confidence,
                    plate=text,
                    plate_confidence=text_confidence,
                    roi_path=roi_path,
                )
            )

        image_processed_path = self._save_processed_img(
            Path(image_name).stem, processed_image, count_classes
        )

        image_processed_cvt = self.convert_cv2_to_pil(processed_image)

        print('DetectPlate - detect_image_classes() - End')

        return image_processed_cvt, image_processed_path, detected_classes
