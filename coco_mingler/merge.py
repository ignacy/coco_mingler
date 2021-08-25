import os

import orjson

from coco_mingler.parser import Parser


class Merge:
    def __init__(self, path, outpath):
        self.path = path
        self.outpath = outpath

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

        with open(self.outpath, "wb") as outfile:
            outfile.write(orjson.dumps(out))
