import unittest
import pytest
from .test_day import DayTest
from advent.advent2022 import day3


@pytest.mark.day
class TestDay3(DayTest):
    test_day = day3.Day3()
    expected_part_1 = "Advent 2022 Day 3 part 1 not yet implemented."
    expected_part_2 = "Advent 2022 Day 3 part 2 not yet implemented."

    def test_split_line(self):
        with self.assertRaises(ValueError):
            day3.split_line("abcde")

        self.assertEqual(day3.split_line("abcd"), ("ab", "cd"))

    def test_find_common_element(self):
        with self.assertRaises(ValueError):
            day3.find_common_element("abc", "de")

        self.assertEqual("c", day3.find_common_element("abc", "dcf"))
        self.assertEqual("c", day3.find_common_element("abc", "dfc"))
