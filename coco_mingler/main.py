import getopt
import orjson
import logging
import os

from coco_mingler.annotations import Annotations
from coco_mingler.exceptions import InvalidArgumentError
from coco_mingler.licenses import Licenses
from coco_mingler.merge import Merge
from coco_mingler.parser import Parser

logger = logging.getLogger("COCO Mingler")
OUTPUT_DIR = 'tmp/images/'

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
            Merge(OUTPUT_DIR).merge()
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

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for image in data["images"]:
        out_file_name = OUTPUT_DIR + image["file_name"] + ".json"

        # TODO scrap unused categories
        image_out = {
            "info": data["info"],
            "categories": data["categories"],
            "images": [image],
            "annotations": [annotations.get(image["id"])],
            "licenses": licenses.get(image["license"])
        }

        with open(out_file_name, "wb") as outfile:
            outfile.write(orjson.dumps(image_out))

    return 0
