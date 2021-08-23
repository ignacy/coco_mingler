from coco_mingler.parser import Parser
from coco_mingler.annotations import Annotations
from coco_mingler.licenses import Licenses

from coco_mingler.exceptions import InvalidArgumentError
import logging, getopt, os, json

logger = logging.getLogger("COCO Mingler")

def main(argv=None):
    """Run the coco_mingler command.

    Args:
        argv: optional list of arguments to parse.
        sys.argv is used by default

    Returns:
        int: command's return code
    """
    inputfile = ''

    try:
        opts, _ = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print('bin/coco_mingler -i <inputfile>')
        return 2
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg

    data = {}

    try:
        data = Parser(inputfile).parse()
    except InvalidArgumentError as e:
        print(e)
        return 2

    # Build dictionaries for annotations and licenses so we don't 
    # have to traverse those collections looking for ID every time
    annotations = Annotations(data['annotations'])
    licenses = Licenses(data['licenses'])

    os.makedirs('tmp/images', exist_ok=True)

    for image in data['images']:
        image_out = {}
        image_out['info'] = data['info']
        image_out['categories'] = data['categories'] # TODO scrap unused categories
        image_out['images'] = [image]
        image_out['annotations'] = [annotations.get(image['id'])]
        image_out['licenses'] = licenses.get(image['license'])

        with open('tmp/images/' + image['file_name'] + '.json', "w") as outfile:
            json_object = json.dumps(image_out, indent = 4)
            outfile.write(json_object)

    return 0
