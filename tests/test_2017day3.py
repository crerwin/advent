import pytest
from .test_day import DayTest
from advent.advent2017 import day3


def test_manhattan_distance():
    assert day3.manhattan_distance((0, 0), (0, 0)) == 0
    assert day3.manhattan_distance((-1, 0), (0, 0)) == 1
    assert day3.manhattan_distance((2, -1), (0, 0)) == 3
    assert day3.manhattan_distance((0, 2), (0, 0)) == 2


def test_find_position():
    assert day3.find_position(1) == (0, 0)
    assert day3.find_position(2) == (1, 0)
    assert day3.find_position(12) == (2, 1)
    assert day3.find_position(16) == (-1, 2)
    assert day3.find_position(23) == (0, -2)


def test_find_retrieval_distance():
    assert day3.find_retrieval_distance(1) == 0
    assert day3.find_retrieval_distance(12) == 3
    assert day3.find_retrieval_distance(23) == 2
    assert day3.find_retrieval_distance(1024) == 31


@pytest.mark.day
class TestDay3(DayTest):
    test_day = day3.Day3()
    expected_part_1 = "475"
