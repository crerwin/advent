import unittest
import pytest

from .test_day import DayTest
from advent.advent2020 import day3


class Day3TestCase(unittest.TestCase):
    def test_load_1(self):
        input = [
            ".**",
            ".*.",
            "..."
        ]
        expected = [
            [".", "*", "*"],
            [".", "*", "."],
            [".", ".", "."]
        ]
        test_day = day3.Day3()
        test_day.load_slope(input)
        self.assertEqual(test_day.slope, expected)

    def test_ski(self):
        test_input = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
        ]
        test_day = day3.Day3()
        test_day.load_slope(test_input)
        self.assertEqual(2, test_day.ski(1, 1))
        self.assertEqual(7, test_day.ski(3, 1))
        self.assertEqual(3, test_day.ski(5, 1))
        self.assertEqual(4, test_day.ski(7, 1))
        self.assertEqual(2, test_day.ski(1, 2))

     
@pytest.mark.day
class TestDay2(DayTest):
    test_day = day3.Day3()
    expected_part_1 = "244"
    expected_part_2 = "9406609920"
