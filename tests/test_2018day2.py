import unittest
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