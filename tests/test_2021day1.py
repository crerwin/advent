import unittest
import pytest
from .test_day import DayTest
from advent.advent2021 import day1


class TestDepthIncreases(unittest.TestCase):
    def test_depth_increases(self):
        inputs = [
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
        self.assertEqual(day1.count_depth_increases(inputs), 7)
