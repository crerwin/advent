import unittest
from advent import day


class DayTest(unittest.TestCase):
    test_day = day.Day()
    expected_part_1 = None
    expected_part_2 = None
    resulting_part_1 = None
    resulting_part_2 = None

    @classmethod
    def setUpClass(cls):
        cls.resulting_part_1 = cls.test_day.part1()
        cls.resulting_part_2 = cls.test_day.part2()

    def setUp(self):
        if not self.expected_part_1:
            self.expected_part_1 = f"Advent {self.test_day.year} Day {self.test_day.day} part 1 not yet implemented."
        if not self.expected_part_2:
            self.expected_part_2 = f"Advent {self.test_day.year} Day {self.test_day.day} part 2 not yet implemented."

    def test_returns_strings(self):
        self.assertIsInstance(self.resulting_part_1, str)
        self.assertIsInstance(self.resulting_part_2, str)

    def test_part_1(self):
        self.assertEqual(self.resulting_part_1, self.expected_part_1)

    def test_part_2(self):
        self.assertEqual(self.resulting_part_2, self.expected_part_2)

    def test_part(self):
        self.assertEqual(self.resulting_part_1, self.expected_part_1)
        self.assertEqual(self.resulting_part_2, self.expected_part_2)
