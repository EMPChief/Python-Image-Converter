from .Basic import Basic


class JpegTransmuting(Basic):
    def __init__(self, image_path, image_output_path):
        super().__init__(image_path, image_output_path)

    def convert(self):
        self._convert_image('JPEG')
