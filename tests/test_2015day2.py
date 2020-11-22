import unittest
from .test_day import DayTest
from advent.advent2015 import day2


class WrapTestCase(unittest.TestCase):
    def test_wrap_case_1(self):
        self.assertEqual(day2.wrap(2, 3, 4), 58)

    def test_wrap_case_2(self):
        self.assertEqual(day2.wrap(1, 1, 10), 43)


class RibbonTestCase(unittest.TestCase):
    def test_ribbon_case1(self):
        self.assertEqual(day2.ribbon(2, 3, 4), 34)

    def test_ribbon_case2(self):
        self.assertEqual(day2.ribbon(1, 1, 10), 14)


class Day2Test(DayTest):
    test_day = day2.Day2()
    expected_part_1 = "1588178"
    expected_part_2 = "3783758"
