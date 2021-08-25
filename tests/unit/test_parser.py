import pytest
from coco_mingler.parser import Parser
from coco_mingler.exceptions import InvalidArgumentError

def test_parses_file_data():
    data = Parser('tests/unit/example.json').parse()
    assert data["a key"] == "a value"

def test_fails_when_it_cant_find_the_file():
    with pytest.raises(InvalidArgumentError):
        Parser('not a valid file path')

