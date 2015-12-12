import unittest
import day3


class SantaOnlyTestCase(unittest.TestCase):
    def test_walk_empty_string(self):
        self.assertEquals(day3.walk(""), 0)

    def test_walk_bad_string(self):
        with self.assertRaises(ValueError):
            day3.walk("your mom")

    def test_walk_case_1(self):
        self.assertEquals(day3.walk(">"), 2)

    def test_walk_case_2(self):
        self.assertEquals(day3.walk("^>v<"), 4)