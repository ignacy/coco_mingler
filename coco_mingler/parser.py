import os

import orjson

from coco_mingler.exceptions import InvalidArgumentError


class Parser:
    def __init__(self, input_file_path):
        if not os.path.isfile(input_file_path):
            message = f"'{input_file_path}' is not a valid file path"
            raise InvalidArgumentError(message)
        self.input_file_path = input_file_path

    def parse(self):
        with open(self.input_file_path, "r") as coco_file:
            data = coco_file.read()

        return orjson.loads(data)
