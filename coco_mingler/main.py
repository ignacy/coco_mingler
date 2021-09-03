import getopt
import logging
import os

import orjson

from coco_mingler.annotations import Annotations
from coco_mingler.exceptions import InvalidArgumentError
from coco_mingler.licenses import Licenses
from coco_mingler.merge import Merge
from coco_mingler.parser import Parser

logger = logging.getLogger("COCO Mingler")
OUTPUT_DIR = "tmp/images/"


def main(argv=None):
    """Run the coco_mingler command.

    Args:
        argv: optional list of arguments to parse.
        sys.argv is used by default

    Returns:
        int: command's return code
    """
    inputfile = ""
    mdir = OUTPUT_DIR
    outpath = OUTPUT_DIR
    split = True

    try:
        opts, _ = getopt.getopt(argv, "o:m:hi:", ["ifile=", "mdir=", "out="])
    except getopt.GetoptError:
        print("SPLIT: bin/coco_mingler -i <inputfile> -o <outputdir>")
        print("MERGE: bin/coco_mingler -m <mdir> -o <outputpath>")
        return 2
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt == "-h":
            print("SPLIT: bin/coco_mingler -i <inputfile> -o <outputdir>")
            print("MERGE: bin/coco_mingler -m <mdir> -o <outputpath>")
            return 0
        elif opt in ("-o", "--out"):
            outpath = arg
        elif opt in ("-m", "--mdir"):
            split = False
            mdir = arg

    if not split:
        print("Merging files into one COCO file")
        Merge(mdir, outpath).merge()
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

    os.makedirs(outpath, exist_ok=True)

    for image in data["images"]:
        out_file_name = outpath + "/" + image["file_name"] + ".json"

        image_out = {
            "info": data["info"],
            "categories": data["categories"],
            "images": [image],
            "annotations": [annotations.get(image["id"])],
            "licenses": licenses.get(image["license"]),
        }

        with open(out_file_name, "wb") as outfile:
            outfile.write(orjson.dumps(image_out))

    return 0
