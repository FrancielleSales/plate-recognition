import easyocr
from typing import Tuple


class PlateTextExtractor:
    def __init__(self):
        self.reader = easyocr.Reader(["pt"])

    def validate_plate(self, text: str) -> bool:
        if text is None or text.strip() == "":
            return False
        # Keep only alphanumeric characters
        if text in ["BR", "BRASIL"]:
            return False
        return True

    def extract_plate_text(self, image) -> Tuple[str, float]:
        plate_text = ""
        confidence = 0.0
        try:
            results = self.reader.readtext(image)

            for bbox, text, conf in results:
                text = text.upper()
                print(f"PlateTextExtractor - extract_plate_text() - Detected text: {text}")
                if self.validate_plate(text) is True:
                    plate_text = text
                    confidence = float(conf)
                    break
        except Exception as e:
            print(f"PlateTextExtractor - extract_plate_text() - An unexpected error occurred: {e}")
        finally:
            return plate_text, confidence
