import json
import os

from coco_mingler.parser import Parser


class Merge:
    def __init__(self, path):
        self.path = path

    def merge(self):
        out = {
            "annotations": [],
            "images": [],
            "categories": [],
            "info": "",
            "licenses": [],
        }

        for filename in os.scandir(self.path):
            if filename.is_file():
                data = Parser(filename.path).parse()
                out["info"] = data["info"]  # TODO: only needed once
                out["categories"] = data["categories"]  # TODO: merge tree
                out["annotations"].append(data["annotations"])
                out["images"].append(data["images"])

        with open("tmp/merged.json", "w") as outfile:
            json_object = json.dumps(out, indent=4)
            outfile.write(json_object)
