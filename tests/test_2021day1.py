import unittest
import pytest
from .test_day import DayTest
from advent.advent2021 import day1


class TestDepthIncreases(unittest.TestCase):
    def setUp(self) -> None:
        self.test_inputs = [
            "199",
            "200",
            "208",
            "210",
            "200",
            "207",
            "240",
            "269",
            "260",
            "263",
        ]

    def test_depth_increases(self):
        self.assertEqual(day1.count_depth_increases(self.test_inputs), 7)

    def test_sliding_window_increases(self):
        self.assertEqual(day1.sliding_window_increases(self.test_inputs), 5)


@pytest.mark.day
class TestDay1(DayTest):
    test_day = day1.Day1()
    expected_part_1 = "1665"
    expected_part_2 = "1702"
