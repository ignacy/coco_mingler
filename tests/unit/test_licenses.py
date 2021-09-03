from coco_mingler.licenses import Licenses


def data():
    return [{"id": 3, "somedata": "A"}, {"id": 2, "somedata": "B"}]


def test_license_can_access_by_id():
    license = Licenses(data())
    on_2 = license.get(2)
    assert on_2 is not None
    assert on_2["somedata"] == "B"


def test_license_does_not_find_data_for_missing_id():
    license = Licenses(data())
    assert license.get(1) is None
