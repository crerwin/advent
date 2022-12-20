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
        self.assertEqual(
            day3.split_line("vJrwpWtwJgWrhcsFMMfFFhFp"),
            ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        )

    def test_find_common_element(self):
        with self.assertRaises(ValueError):
            day3.find_common_element("abc", "de")

        with self.assertRaises(ValueError):
            day3.find_common_element("abacad", "afabah")

        self.assertEqual("c", day3.find_common_element("abc", "dcf"))
        self.assertEqual("c", day3.find_common_element("abc", "dfc"))
        self.assertEqual("p", day3.find_common_element("vJrwpWtwJgWr", "hcsFMMfFFhFp"))
        self.assertEqual(
            "L", day3.find_common_element("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")
        )

    def test_get_item_priority(self):
        with self.assertRaises(ValueError):
            day3.get_item_priority("aa")

        self.assertEqual(1, day3.get_item_priority("a"))
        self.assertEqual(25, day3.get_item_priority("y"))
        self.assertEqual(26, day3.get_item_priority("z"))
        self.assertEqual(27, day3.get_item_priority("A"))
        self.assertEqual(52, day3.get_item_priority("Z"))

    def test_get_priorities_sum(self):
        test_data = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
        self.assertEqual(157, day3.get_priorities_sum(test_data))
