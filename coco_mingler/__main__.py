"""Main entry point for the COCO mingler command line tool."""
import sys

from coco_mingler.main import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
