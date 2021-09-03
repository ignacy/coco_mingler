import os

import orjson

from coco_mingler.parser import Parser


class Merge:
    def __init__(self, path, outpath):
        self.path = path
        self.outpath = outpath

    def merge(self):
        """Merge COCO files in path into one COCO file at outpath"""

        out = {
            "annotations": [],
            "images": [],
            "categories": [],
            "info": "",
            "licenses": {},
        }

        for filename in os.scandir(self.path):
            if filename.is_file():
                data = Parser(filename.path).parse()
                out["info"] = data["info"]
                out["categories"] = data["categories"]
                out["annotations"].extend(data["annotations"])
                out["licenses"][data["licenses"]["id"]] = data["licenses"]
                out["images"].extend(data["images"])

        # Remove duplicated license records
        out["licenses"] = list(out["licenses"].values())

        with open(self.outpath, "wb") as outfile:
            outfile.write(orjson.dumps(out))
