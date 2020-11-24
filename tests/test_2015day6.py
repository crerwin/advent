import unittest
import pytest
from tests.test_day import DayTest
from advent.advent2015 import day6


class ParseLineTestCase(unittest.TestCase):
    def test1(self):
        result = day6.parseline("turn off 660,55 through 986,197")
        self.assertEqual(result[0], "off")
        self.assertEqual(result[1], 660)
        self.assertEqual(result[2], 55)
        self.assertEqual(result[3], 986)
        self.assertEqual(result[4], 197)


class ActTestCase(unittest.TestCase):
    def test1(self):
        result = day6.parseline("turn on 0,0 through 999,999")
        testarray = day6.LightArray()
        testarray.act(*result)
        self.assertEqual(testarray.get_lit_count(), 1000000)

    def test2(self):
        result = day6.parseline("toggle 0,0 through 999,0")
        testarray = day6.LightArray()
        testarray.act(*result)
        self.assertEqual(testarray.get_lit_count(), 1000)

    def test3(self):
        result = day6.parseline("toggle 499,499 through 500,500")
        testarray = day6.LightArray()
        testarray.act(*result)
        self.assertEqual(testarray.get_lit_count(), 4)


class Part2TestCase(unittest.TestCase):
    def test1(self):
        result = day6.parseline("turn on 0,0 through 0,0")
        testarray = day6.Part2Array()
        testarray.act(*result)
        self.assertEqual(testarray.get_brightness(), 1)

    def test2(self):
        result = day6.parseline("toggle 0,0 through 999,999")
        testarray = day6.Part2Array()
        testarray.act(*result)
        self.assertEqual(testarray.get_brightness(), 2000000)

    def test3(self):
        result = day6.parseline("turn off 499,499 through 500,500")
        testarray = day6.Part2Array()
        testarray.act(*result)
        self.assertEqual(testarray.get_brightness(), 0)


@pytest.mark.day
class Day6Test(DayTest):
    test_day = day6.Day6()
    expected_part_1 = "400410"
    expected_part_2 = "15343601"
