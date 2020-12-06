import unittest
import pytest
from .test_day import DayTest
from advent.advent2020 import day2


class PwTestCase(unittest.TestCase):
    def test_get_min(self):
        self.assertEqual(day2.get_min("1-3 a: abcde"), 1)
        self.assertEqual(day2.get_min("1-3 b: cdefg"), 1)
        self.assertEqual(day2.get_min("2-9 c: ccccccccc"), 2)
        self.assertEqual(day2.get_min("2483-9 c: ccccccccc"), 2483)

    def test_get_max(self):
        self.assertEqual(day2.get_max("1-3 a: abcde"), 3)
        self.assertEqual(day2.get_max("1-3 b: cdefg"), 3)
        self.assertEqual(day2.get_max("2-9 c: ccccccccc"), 9)
        self.assertEqual(day2.get_max("2-9478 c: ccccccccc"), 9478)

    def test_get_required_char(self):
        self.assertEqual(day2.get_required_char("1-3 a: abcde"), "a")
        self.assertEqual(day2.get_required_char("1-3 b: cdefg"), "b")
        self.assertEqual(day2.get_required_char("2-9 c: ccccccccc"), "c")

    def test_get_password(self):
        self.assertEqual(day2.get_password("1-3 a: abcde"), "abcde")
        self.assertEqual(day2.get_password("1-3 b: cdefg"), "cdefg")
        self.assertEqual(day2.get_password("2-9 c: ccccccccc"), "ccccccccc")

    def test_is_valid(self):
        self.assertTrue(day2.is_valid("1-3 a: abcde"))
        self.assertFalse(day2.is_valid("1-3 b: cdefg"))
        self.assertTrue(day2.is_valid("2-9 c: ccccccccc"))

    def test_is_valid_2(self):
        self.assertTrue(day2.is_valid_2("1-3 a: abcde"))
        self.assertFalse(day2.is_valid_2("1-3 b: cdefg"))
        self.assertFalse(day2.is_valid_2("2-9 c: ccccccccc"))

    def test_count_valid(self):
        inputs = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        self.assertEqual(day2.count_valid(inputs), 2)

    def test_count_valid_2(self):
        inputs = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        self.assertEqual(day2.count_valid_2(inputs), 1)


@pytest.mark.day
class TestDay2(DayTest):
    test_day = day2.Day2()
    expected_part_1 = "636"
    expected_part_2 = "588"
