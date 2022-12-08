import unittest
import pytest
from .test_day import DayTest
from advent.advent2022 import day1


class TestFindHighestCalorieCount(unittest.TestCase):
    def setUp(self) -> None:
        self.test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    def test_find_highest_calorie_count(self):
        self.assertEqual(
            day1.find_highest_calorie_count(self.test_input.splitlines()), 24000
        )

    def test_find_top_three_calorie_counts(self):
        self.assertEqual(
            day1.find_top_three_calorie_counts(self.test_input.splitlines()), 45000
        )


@pytest.mark.day
class TestDay1(DayTest):
    test_day = day1.Day1()
    expected_part_1 = "74394"
    expected_part_2 = "212836"
