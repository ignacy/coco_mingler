from coco_mingler.parser import Parser

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

    annotations_dict = {}
    for annotation in data['annotations']:
        annotations_dict[annotation['image_id']] = annotation
    
    licenses_dict = {}
    for license in data['licenses']:
        licenses_dict[license['id']] = license


    os.makedirs('tmp/images', exist_ok=True)

    for image in data['images'][0:2]:
        image_out = {}
        image_out['info'] = data['info']
        image_out['categories'] = data['categories']
        image_out['images'] = [image]
        image_out['annotations'] = [annotations_dict[image['id']]]
        image_out['licenses'] = licenses_dict[image['license']]

        with open('tmp/images/' + image['file_name'] + '.json', "w") as outfile:
            json_object = json.dumps(image_out, indent = 4)
            outfile.write(json_object)

    return 0
