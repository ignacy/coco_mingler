![example workflow](https://github.com/ignacy/coco_mingler/actions/workflows/pre-commit.yml/badge.svg)

### COCO Mingler

COCO “Common Objects In Context” is a file format for storing datasets for computer vision. You can find detailed description [here](https://towardsdatascience.com/getting-started-with-coco-dataset-82def99fa0b8).

COCO files can be really large and this script helps to solve that problem by providing a tool for splitting them into multiple files (one per each image) and also merging them back together.


### Usage

1. To run tests:

```sh
python -m tests
```

2. To split COCO file into smaller ones:

```sh
bin/coco_mingler -i <path> -o <outputdir>

# Example:

bin/coco_mingler -i data/instances_minitrain2017.json -o tmp/images
```

Files will end up in `tmp/images` if `-o` is not specified

3. To merge files into one COCO file

```sh
bin/coco_mingler -m <path_to_directory> -o <outputfile>

# Example:

bin/coco_mingler -m tmp/images -o tmp/merged.json
```
