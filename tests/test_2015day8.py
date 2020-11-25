import pytest
from tests.test_day import DayTest
from advent.advent2015 import day8


@pytest.mark.day
class Day8Test(DayTest):
    test_day = day8.Day8()
    expected_part_1 = "1333"
    expected_part_2 = "2046"
