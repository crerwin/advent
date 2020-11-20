import unittest
from advent import day


class DayTest(unittest.TestCase):
    test_day = day.Day()
    expected_part_1 = "not yet implemented"
    expected_part_2 = "not yet implemented"

    def test_returns_strings(self):
        self.assertIsInstance(self.test_day.part1(), str)
        self.assertIsInstance(self.test_day.part2(), str)

    def test_part_1(self):
        self.assertEqual(self.test_day.part1(), self.expected_part_1)

    def test_part_2(self):
        self.assertEqual(self.test_day.part2(), self.expected_part_2)

    def test_part(self):
        self.assertEqual(self.test_day.part(1), self.expected_part_1)
        self.assertEqual(self.test_day.part(2), self.expected_part_2)
