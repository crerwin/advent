import unittest
import pytest
from tests.test_day import DayTest
from advent.advent2015 import day11


class PasswordTestCase(unittest.TestCase):
    def test_rule_1_1(self):
        self.test_password = day11.Password("abcddddd")
        self.assertEqual(True, self.test_password.meets_requirement_1())

    def test_rule_1_2(self):
        self.test_password = day11.Password("aeiopqff")
        self.assertEqual(True, self.test_password.meets_requirement_1())

    def test_rule_1_3(self):
        self.test_password = day11.Password("ghjaaabb")
        self.assertEqual(False, self.test_password.meets_requirement_1())

    def test_rule_2_1(self):
        self.test_password = day11.Password("abcdefgh")
        self.assertEqual(True, self.test_password.meets_requirement_2())

    def test_rule_2_2(self):
        self.test_password = day11.Password("abcdefgi")
        self.assertEqual(False, self.test_password.meets_requirement_2())

    def test_rule_2_3(self):
        self.test_password = day11.Password("abcdefgo")
        self.assertEqual(False, self.test_password.meets_requirement_2())

    def test_rule_2_4(self):
        self.test_password = day11.Password("abcdefgl")
        self.assertEqual(False, self.test_password.meets_requirement_2())

    def test_rule_3_1(self):
        self.test_password = day11.Password("abcdefgh")
        self.assertEqual(False, self.test_password.meets_requirement_3())

    def test_rule_3_2(self):
        self.test_password = day11.Password("aabbcdef")
        self.assertEqual(True, self.test_password.meets_requirement_3())

    def test_rule_3_3(self):
        self.test_password = day11.Password("abbcddef")
        self.assertEqual(True, self.test_password.meets_requirement_3())

    def test_rule_3_4(self):
        self.test_password = day11.Password("abcccefg")
        self.assertEqual(False, self.test_password.meets_requirement_3())

    def test_rule_3_5(self):
        self.test_password = day11.Password("aabcdeaa")
        self.assertEqual(False, self.test_password.meets_requirement_3())

    def test_combo_1(self):
        self.test_password = day11.Password("hijklmmn")
        self.assertEqual(True, self.test_password.meets_requirement_1())
        self.assertEqual(False, self.test_password.meets_requirement_2())

    def test_combo_2(self):
        self.test_password = day11.Password("abbceffg")
        self.assertEqual(False, self.test_password.meets_requirement_1())
        self.assertEqual(True, self.test_password.meets_requirement_3())

    def test_is_valid_1(self):
        self.test_password = day11.Password("abbcegjk")
        self.assertEqual(False, self.test_password.is_valid())

    def test_is_valid_2(self):
        self.test_password = day11.Password("abcdffaa")
        self.assertEqual(True, self.test_password.is_valid())

    def test_is_valid_3(self):
        self.test_password = day11.Password("ghjaabcc")
        self.assertEqual(True, self.test_password.is_valid())

    def test_increment_character_1(self):
        self.test_password = day11.Password("aaaaaaaa")
        self.assertEqual("b", self.test_password.increment_character("a"))
        self.assertEqual("g", self.test_password.increment_character("f"))
        self.assertEqual("a", self.test_password.increment_character("z"))
        self.assertEqual("j", self.test_password.increment_character("h"))
        self.assertEqual("p", self.test_password.increment_character("n"))
        self.assertEqual("m", self.test_password.increment_character("k"))

    def test_increment_password_1(self):
        self.test_password = day11.Password("aaaaaaaa")
        self.test_password.increment_password()
        self.assertEqual("aaaaaaab", self.test_password.get_password())

    def test_increment_password_2(self):
        self.test_password = day11.Password("aaaaaaaz")
        self.test_password.increment_password()
        self.assertEqual("aaaaaaba", self.test_password.get_password())

    def test_increment_password_3(self):
        self.test_password = day11.Password("zzzzzzzz")
        self.test_password.increment_password()
        self.assertEqual("aaaaaaaa", self.test_password.get_password())

    def test_increment_password_4(self):
        self.test_password = day11.Password("aazzaazz")
        self.test_password.increment_password()
        self.assertEqual("aazzabaa", self.test_password.get_password())

    def test_find_next_password_1(self):
        self.test_password = day11.Password("abcdefgh")
        self.test_password.find_next_password()
        self.assertEqual("abcdffaa", self.test_password.get_password())

    def test_find_next_password_2(self):
        self.test_password = day11.Password("ghijklmn")
        self.test_password.find_next_password()
        self.assertEqual("ghjaabcc", self.test_password.get_password())

@pytest.mark.day
class Day11Test(DayTest):
    test_day = day11.Day11()
    expected_part_1 = "vzbxxyzz"
    expected_part_2 = "vzcaabcc"
