import unittest
import pytest
from .test_day import DayTest
from advent.advent2018 import day2


class RulesTestCase(unittest.TestCase):
    def test_exactly_two(self):
        self.assertTrue(day2.exactly_two_of_any_letter("bababc"))
        self.assertTrue(day2.exactly_two_of_any_letter("abbcde"))
        self.assertTrue(day2.exactly_two_of_any_letter("aabcdd"))
        self.assertTrue(day2.exactly_two_of_any_letter("abcdee"))

        self.assertFalse(day2.exactly_two_of_any_letter("abcdef"))
        self.assertFalse(day2.exactly_two_of_any_letter("abcccd"))
        self.assertFalse(day2.exactly_two_of_any_letter("ababab"))

    def test_exactly_three(self):
        self.assertTrue(day2.exactly_three_of_any_letter("bababc"))
        self.assertTrue(day2.exactly_three_of_any_letter("abcccd"))
        self.assertTrue(day2.exactly_three_of_any_letter("ababab"))

        self.assertFalse(day2.exactly_three_of_any_letter("abcdef"))
        self.assertFalse(day2.exactly_three_of_any_letter("abbcde"))
        self.assertFalse(day2.exactly_three_of_any_letter("aabcdd"))
        self.assertFalse(day2.exactly_three_of_any_letter("abcdee"))

    def test_get_common_chars(self):
        self.assertEqual(day2.get_common_chars("", ""), "")
        self.assertEqual(day2.get_common_chars("abc", "dbe"), "b")
        self.assertEqual(day2.get_common_chars("abcde", "axcye"), "ace")
        self.assertEqual(day2.get_common_chars("fghij", "fguij"), "fgij")

    def test_get_common_chars_bad_input(self):
        with self.assertRaises(ValueError):
            day2.get_common_chars("abc", "de")

        with self.assertRaises(ValueError):
            day2.get_common_chars("abc", "defg")


@pytest.mark.day
class TestDay2(DayTest):
    test_day = day2.Day2()
    expected_part_1 = "4693"
    expected_part_2 = "pebjqsalrdnckzfihvtxysomg"
