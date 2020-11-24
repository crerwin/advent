import unittest
import pytest
from .test_day import DayTest
from advent.advent2018 import day1


class WalkTestCase(unittest.TestCase):
    def test_step_1(self):
        self.assertEqual(day1.step(0, "+1"), 1)

    def test_walk_1(self):
        self.assertEqual(day1.walk(0, ["+1", "+1", "+1"]), 3)
        self.assertEqual(day1.walk(0, ["+1", "+1", "-2"]), 0)
        self.assertEqual(day1.walk(0, ["-1", "-2", "-3"]), -6)

    def test_find_repeated_frequency(self):
        self.assertEqual(day1.find_repeated_frequency(0, ["+1", "-1"]), 0)
        self.assertEqual(
            day1.find_repeated_frequency(0, ["+3", "+3", "+4", "-2", "-4"]), 10
        )
        self.assertEqual(
            day1.find_repeated_frequency(0, ["-6", "+3", "+8", "+5", "-6"]), 5
        )
        self.assertEqual(
            day1.find_repeated_frequency(0, ["+7", "+7", "-2", "-7", "-4"]), 14
        )


@pytest.mark.day
class Day1Test(DayTest):
    test_day = day1.Day1()
    expected_part_1 = "561"
    expected_part_2 = "563"
