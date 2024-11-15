import os
import cv2


class SaveFile:
    def __init__(self):
        pass

    def verify_path(self, path: str) -> bool:
        if not os.path.exists(path):
            try:
                print('Creating image output path')
                os.makedirs(path, exist_ok=True)
            except OSError as e:
                print(f"OS error while verifying path '{path}': {e}")
                return False
            except Exception as e:
                print(
                    f"An unexpected error occurred while verifying path '{path}': {e}"
                )
                return False
        return True

    def save_image(self, path: str, image_name: str, image_data: cv2) -> str:
        try:
            if self.verify_path(path) is False:
                return ""

            file_path = f"{path}/{image_name}"

            cv2.imwrite(file_path, image_data)

            return file_path
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return ""
