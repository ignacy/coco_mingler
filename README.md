![example workflow](https://github.com/ignacy/coco_mingler/actions/workflows/pre-commit.yml/badge.svg)

### COCO Mingler

This repository solves problems described in this gist https://gist.github.com/volkfox/4c878862a7887a83c2d57f82069e5968


### Usage

1. To run tests:

```
python -m tests
```

2. To split COCO file into smaller ones:

```
bin/coco_mingler -i <path> -o <outputdir>

# Example:

bin/coco_mingler -i data/instances_minitrain2017.json -o tmp/images
```

Files will end up in `tmp/images` if `-o` is not specified

3. To merge files into one COCO file

```
bin/coco_mingler -m <path_to_directory> -o <outputfile>

# Example:

bin/coco_mingler -m tmp/images -o tmp/merged.json
```
