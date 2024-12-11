import unittest
import pytest
from .test_day import DayTest
from advent.advent2024 import day1

@pytest.mark.day
class TestDay1(DayTest):
    test_day = day1.Day1()
    expected_part_1 = "1873376"
    expected_part_2 = "Advent 2024 Day 1 part 2 not yet implemented."

    def test_get_distance(self):
        self.assertEqual(self.test_day.get_distance(1, 3), 2)
        self.assertEqual(self.test_day.get_distance(3, 1), 2)
        self.assertEqual(self.test_day.get_distance(2, 3), 1)
        self.assertEqual(self.test_day.get_distance(3, 3), 0)

    def test_get_total_distance_between_lists(self):
        with self.assertRaises(ValueError):
            self.test_day.get_total_distance_between_lists([1, 2, 3], [4, 5])

        test_list_a = [3, 4, 2, 1, 3, 3]
        test_list_b = [4, 3, 5, 3, 9, 3]

        test_list_a.sort()
        test_list_b.sort()
        self.assertEqual(self.test_day.get_total_distance_between_lists(test_list_a, test_list_b), 11)

    def test_get_similarity_score(self):
        test_list_a = [3, 4, 2, 1, 3, 3]
        test_list_b = [4, 3, 5, 3, 9, 3]
        self.assertEqual(self.test_day.get_similarity_score(test_list_a, test_list_b), 31)

    def test_load_lists_from_input(self):
        self.test_day.reset_lists()
        self.assertEqual(self.test_day.list_a, [])
        self.assertEqual(self.test_day.list_b, [])

        test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
        self.test_day.load_lists_from_input(test_input)
        self.assertEqual(self.test_day.list_a, [3, 4, 2, 1, 3, 3])
        self.assertEqual(self.test_day.list_b, [4, 3, 5, 3, 9, 3])
        self.test_day.list_a.sort()
        self.test_day.list_b.sort()
        self.assertEqual(self.test_day.get_total_distance_between_lists(self.test_day.list_a, self.test_day.list_b), 11)