import unittest
from days import day11

class PasswordTestCase(unittest.TestCase):
    def test_rule_1_1(self):
        self.test_password = day11.password("abcddddd")
        self.assertEqual(True, self.test_password.meets_requirement_1())

    def test_rule_1_2(self):
        self.test_password = day11.password("aeiopqff")
        self.assertEqual(True, self.test_password.meets_requirement_1())

    def test_rule_2_1(self):
        self.test_password = day11.password("abcdefgh")
        self.assertEqual(True, self.test_password.meets_requirement_2())

    def test_rule_2_2(self):
        self.test_password = day11.password("abcdefgi")
        self.assertEqual(False, self.test_password.meets_requirement_2())

    def test_rule_2_3(self):
        self.test_password = day11.password("abcdefgo")
        self.assertEqual(False, self.test_password.meets_requirement_2())

    def test_rule_2_4(self):
        self.test_password = day11.password("abcdefgl")
        self.assertEqual(False, self.test_password.meets_requirement_2())

    def test_rule_3_1(self):
        self.test_password = day11.password("abcdefgh")
        self.assertEqual(False, self.test_password.meets_requirement_3())

    def test_rule_3_2(self):
        self.test_password = day11.password("aabbcdef")
        self.assertEqual(True, self.test_password.meets_requirement_3())

    def test_rule_3_3(self):
        self.test_password = day11.password("abbcddef")
        self.assertEqual(True, self.test_password.meets_requirement_3())

    def test_rule_3_4(self):
        self.test_password = day11.password("abcccefg")
        self.assertEqual(False, self.test_password.meets_requirement_3())

    def test_combo_1(self):
        self.test_password = day11.password("hijklmmn")
        self.assertEqual(True, self.test_password.meets_requirement_1())
        self.assertEqual(False, self.test_password.meets_requirement_2())

    def test_combo_2(self):
        self.test_password = day11.password("abbceffg")
        self.assertEqual(False, self.test_password.meets_requirement_1())
        self.assertEqual(True, self.test_password.meets_requirement_3())

    def test_is_valid_1(self):
        self.test_password = day11.password("abbcegjk")
        self.assertEqual(False, self.test_password.is_valid())

    def test_increment_character_1(self):
        self.test_password = day11.password("aaaaaaaa")
        self.assertEqual("b", self.test_password.increment_character("a"))
        self.assertEqual("g", self.test_password.increment_character("f"))
        self.assertEqual("a", self.test_password.increment_character("z"))

    def test_increment_password_1(self):
        self.test_password = day11.password("aaaaaaaa")
        self.test_password.increment_password()
        self.assertEqual("aaaaaaab", self.test_password.get_password)
