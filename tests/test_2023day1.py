import unittest
import pytest
from .test_day import DayTest
from advent.advent2023 import day1


@pytest.mark.day
class TestDay1(DayTest):
    test_day = day1.Day1()
    expected_part_1 = "54304"
    expected_part_2 = "Advent 2023 Day 1 part 2 not yet implemented."

    def test_get_calibration_digit(self):
        with self.assertRaises(ValueError):
            self.test_day._get_calibration_digit("abcde")

        self.assertEqual(self.test_day._get_calibration_digit("abc3de"), "3")
        self.assertEqual(self.test_day._get_calibration_digit("abc3de", True), "3")

        self.assertEqual(self.test_day._get_calibration_digit("1abc2"), "1")
        self.assertEqual(self.test_day._get_calibration_digit("1abc2", True), "2")

        self.assertEqual(self.test_day._get_calibration_digit("pqr3stu8vwx"), "3")
        self.assertEqual(self.test_day._get_calibration_digit("pqr3stu8vwx", True), "8")

        self.assertEqual(self.test_day._get_calibration_digit("a1b2c3d4e5f"), "1")
        self.assertEqual(self.test_day._get_calibration_digit("a1b2c3d4e5f", True), "5")

        self.assertEqual(self.test_day._get_calibration_digit("treb7uchet"), "7")
        self.assertEqual(self.test_day._get_calibration_digit("treb7uchet", True), "7")

    def test_get_calibration_values(self):
        with self.assertRaises(ValueError):
            self.test_day._get_calibration_values("abcde")

        self.assertEqual(self.test_day._get_calibration_values("abc3de"), 33)
        self.assertEqual(self.test_day._get_calibration_values("1abc2"), 12)
        self.assertEqual(self.test_day._get_calibration_values("pqr3stu8vwx"), 38)
        self.assertEqual(self.test_day._get_calibration_values("a1b2c3d4e5f"), 15)
        self.assertEqual(self.test_day._get_calibration_values("treb7uchet"), 77)

    def test_get_calibration_sum(self):
        bad_data = []
        bad_data_2 = ["abcde"]
        bad_data_3 = ["abcde", "efghi"]
        bad_data_4 = ["abcde", "ef2gh4i"]
        test_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

        with self.assertRaises(ValueError):
            self.test_day._get_calibration_sum(bad_data)

        with self.assertRaises(ValueError):
            self.test_day._get_calibration_sum(bad_data_2)

        with self.assertRaises(ValueError):
            self.test_day._get_calibration_sum(bad_data_3)

        with self.assertRaises(ValueError):
            self.test_day._get_calibration_sum(bad_data_4)

        self.assertEqual(self.test_day._get_calibration_sum(test_data), 142)
