import os
import pytest
import csv
from solution import solution
from config import filename

def test_create_file():
    if os.path.exists(filename):
        os.remove(filename)
    solution()
    assert os.path.exists(filename)


def test_animal_count():
    with open(filename, mode='r', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        row = next(reader)
        letter, count = row
        assert letter == 'А'
        assert int(count) == 1298
        row = next(reader)
        letter, count = row
        assert letter == 'Б'
        assert int(count) == 1779
