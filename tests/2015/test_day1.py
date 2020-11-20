import unittest
from tests.test_day import DayTest
from advent.advent2015 import day1


class WalkTestCase(DayTest):
    def setUp(self):
        self.test_day = day1.Day1()
        self.expected_part_1 = 232
        self.expected_part_2 = 1783

    def test_walk_case_1(self):
        result = day1.walk("(())")
        self.assertEqual(result["floor"], 0)

    def test_walk_case_2(self):
        result = day1.walk("()()")
        self.assertEqual(result["floor"], 0)

    def test_walk_case_3(self):
        result = day1.walk("(((")
        self.assertEqual(result["floor"], 3)

    def test_walk_case_4(self):
        result = day1.walk("(()(()(")
        self.assertEqual(result["floor"], 3)

    def test_walk_case_5(self):
        result = day1.walk("))(((((")
        self.assertEqual(result["floor"], 3)

    def test_walk_case_6(self):
        result = day1.walk("())")
        self.assertEqual(result["floor"], -1)

    def test_walk_case_7(self):
        result = day1.walk("))(")
        self.assertEqual(result["floor"], -1)

    def test_walk_case_8(self):
        result = day1.walk(")))")
        self.assertEqual(result["floor"], -3)

    def test_walk_case_9(self):
        result = day1.walk(")())())")
        self.assertEqual(result["floor"], -3)

    def test_walk_case_10(self):
        result = day1.walk(")")
        self.assertEqual(result["basementchar"], 1)

    def test_walk_case_11(self):
        result = day1.walk("()())")
        self.assertEqual(result["basementchar"], 5)


# class Day1TestCase(unittest.TestCase):
#     def setUp(self):
#         self.day = day1.Day1()

#     def test_part_1(self):
#         self.assertEqual(self.day.part(1), 232)

#     def test_part_2(self):
#         self.assertEqual(self.day.part(2), 1783)
