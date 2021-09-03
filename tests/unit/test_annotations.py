from coco_mingler.annotations import Annotations


def data():
    return [{"image_id": 10, "key": "A"}, {"image_id": 22, "key": "B"}]


def test_annotation_can_access_by_image_id():
    annotation = Annotations(data())
    on_22 = annotation.get(22)
    assert on_22 is not None
    assert on_22["key"] == "B"


def test_annotation_does_not_find_data_for_missing_id():
    annotation = Annotations(data())
    assert annotation.get(1) is None
