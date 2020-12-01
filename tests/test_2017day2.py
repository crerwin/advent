import pytest
from .test_day import DayTest
from advent.advent2017 import day2


def test_row_to_ints():
    assert day2.row_to_ints("5 1 9 5") == [5, 1, 9, 5]


def test_checksum_row():
    assert day2.checksum_row([5, 1, 9, 5]) == 8
    assert day2.checksum_row([7, 5, 3]) == 4
    assert day2.checksum_row([2, 4, 6, 8]) == 6


def test_checksum_row2():
    assert day2.checksum_row2([5, 9, 2, 8]) == 4
    assert day2.checksum_row2([9, 4, 7, 3]) == 3
    assert day2.checksum_row2([3, 8, 6, 5]) == 2


def test_checksum():
    input = """5 1 9 5
7 5 3
2 4 6 8"""
    assert day2.checksum(input) == 18


def test_checksum2():
    input = """
5 9 2 8
9 4 7 3
3 8 6 5
"""
    assert day2.checksum2(input) == 9


@pytest.mark.day
class TestDay2(DayTest):
    test_day = day2.Day2()
    expected_part_1 = "41919"
    expected_part_2 = "303"
