import unittest
import day11

class PasswordTestCase(unittest.TestCase):
    def test_rule_1_1(self):
        self.test_password = day11.password("abcddddd")
        self.assertEquals(True, self.test_password.meets_requirement_1())

    def test_rule_1_2(self):
        self.test_password = day11.password("aeiopqff")
        self.assertEquals(True, self.test_password.meets_requirement_1())

    def test_rule_2_1(self):
        self.test_password = day11.password("abcdefgh")
        self.assertEquals(True, self.test_password.meets_requirement_2())

    def test_rule_2_2(self):
        self.test_password = day11.password("abcdefgi")
        self.assertEquals(False, self.test_password.meets_requirement_2())

    def test_rule_2_3(self):
        self.test_password = day11.password("abcdefgo")
        self.assertEquals(False, self.test_password.meets_requirement_2())

    def test_rule_2_4(self):
        self.test_password = day11.password("abcdefgl")
        self.assertEquals(False, self.test_password.meets_requirement_2())

    def test_rule_3_1(self):
        self.test_password = day11.password("abcdefgh")
        self.assertEquals(False, self.test_password.meets_requirement_3())

    def test_rule_3_2(self):
        self.test_password = day11.password("aabbcdef")
        self.assertEquals(True, self.test_password.meets_requirement_3())

    def test_rule_3_3(self):
        self.test_password = day11.password("abbcddef")
        self.assertEquals(True, self.test_password.meets_requirement_3())

    def test_rule_3_4(self):
        self.test_password = day11.password("abcccefg")
        self.assertEquals(False, self.test_password.meets_requirement_3())

    def test_combo_1(self):
        self.test_password = day11.password("hijklmmn")
        self.assertEquals(True, self.test_password.meets_requirement_1())
        self.assertEquals(False, self.test_password.meets_requirement_2())

    def test_combo_2(self):
        self.test_password = day11.password("abbceffg")
        self.assertEquals(False, self.test_password.meets_requirement_1())
        self.assertEquals(True, self.test_password.meets_requirement_3())