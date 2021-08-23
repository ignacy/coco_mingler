import getopt
import json
import logging
import os

from coco_mingler.annotations import Annotations
from coco_mingler.exceptions import InvalidArgumentError
from coco_mingler.licenses import Licenses
from coco_mingler.merge import Merge
from coco_mingler.parser import Parser

logger = logging.getLogger("COCO Mingler")


def main(argv=None):
    """Run the coco_mingler command.

    Args:
        argv: optional list of arguments to parse.
        sys.argv is used by default

    Returns:
        int: command's return code
    """
    inputfile = ""

    try:
        opts, _ = getopt.getopt(argv, "mhi:", ["ifile="])
    except getopt.GetoptError:
        print("bin/coco_mingler -i <inputfile>")
        return 2
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt == "-m":
            print("Merging files into one COCO file")
            Merge("tmp/images").merge()
            return 0

    data = {}

    try:
        data = Parser(inputfile).parse()
    except InvalidArgumentError as e:
        print(e)
        return 2

    # Build dictionaries for annotations and licenses so we don't
    # have to traverse those collections looking for ID every time
    annotations = Annotations(data["annotations"])
    licenses = Licenses(data["licenses"])

    os.makedirs("tmp/images", exist_ok=True)

    for image in data["images"]:
        image_out = {}
        image_out["info"] = data["info"]
        # TODO scrap unused categories
        image_out["categories"] = data["categories"]
        image_out["images"] = [image]
        image_out["annotations"] = [annotations.get(image["id"])]
        image_out["licenses"] = licenses.get(image["license"])

        out_file_name = "tmp/images/" + image["file_name"] + ".json"
        with open(out_file_name, "w") as outfile:
            json_object = json.dumps(image_out, indent=4)
            outfile.write(json_object)

    return 0
