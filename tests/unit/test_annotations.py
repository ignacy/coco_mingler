import pytest
from coco_mingler.annotations import Annotations

def data():
    return [
        { "image_id": 10, "somedata": "A" },
        { "image_id": 22, "somedata": "B" }
    ]

def test_annotation_can_access_by_image_id():
    annotation = Annotations(data())
    assert annotation.get(22)["somedata"] == "B"

def test_annotation_does_not_find_data_for_missing_id():
    annotation = Annotations(data())
    assert annotation.get(1) == None

