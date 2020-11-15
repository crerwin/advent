import unittest
from advent.days import day3


class SantaOnlyTestCase(unittest.TestCase):
    def test_walk_empty_string(self):
        self.assertEqual(day3.walk(""), 0)

    def test_walk_bad_string(self):
        with self.assertRaises(ValueError):
            day3.walk("your mom")

    def test_walk_case_1(self):
        self.assertEqual(day3.walk(">"), 2)

    def test_walk_case_2(self):
        self.assertEqual(day3.walk("^>v<"), 4)


class SantaAndRoboSantaTestCase(unittest.TestCase):
    def test_walk_empty_string(self):
        self.assertEqual(day3.walk("", "part2"), 0)

    def test_walk_bad_string(self):
        with self.assertRaises(ValueError):
            day3.walk("your mom goes to college", "part2")

    def test_walk_case_1(self):
        self.assertEqual(day3.walk("^v", "part2"), 3)

    def test_walk_case_2(self):
        self.assertEqual(day3.walk("^>v<", "part2"), 3)

    def test_walk_case_3(self):
        self.assertEqual(day3.walk("^v^v^v^v^v", "part2"), 11)
