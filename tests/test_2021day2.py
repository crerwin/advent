import unittest
import pytest
from .test_day import DayTest
from advent.advent2021 import day2


class TestDayFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.test_day = day2.Day2()

    def test_valid_instruction(self):
        self.assertTrue(self.test_day.valid_instruction("forward 5"))
        self.assertTrue(self.test_day.valid_instruction("down 5"))
        self.assertTrue(self.test_day.valid_instruction("forward 8"))
        self.assertTrue(self.test_day.valid_instruction("up 3"))
        self.assertTrue(self.test_day.valid_instruction("down 8"))
        self.assertTrue(self.test_day.valid_instruction("forward 2"))

        self.assertFalse(self.test_day.valid_instruction("forward 5 hi"))
        self.assertFalse(self.test_day.valid_instruction("back 3"))
        self.assertFalse(self.test_day.valid_instruction("3 3"))
        self.assertFalse(self.test_day.valid_instruction("forward hi"))
        self.assertFalse(self.test_day.valid_instruction("forward three"))

    def test_move_submarine(self):
        self.test_day.move_submarine("forward 5")
        self.assertEqual(self.test_day.horizontal_position, 5)
        self.assertEqual(self.test_day.depth, 0)

        self.test_day.move_submarine("down 5")
        self.assertEqual(self.test_day.horizontal_position, 5)
        self.assertEqual(self.test_day.depth, 5)

        self.test_day.move_submarine("forward 8")
        self.assertEqual(self.test_day.horizontal_position, 13)
        self.assertEqual(self.test_day.depth, 5)

        self.test_day.move_submarine("up 3")
        self.assertEqual(self.test_day.horizontal_position, 13)
        self.assertEqual(self.test_day.depth, 2)

        self.test_day.move_submarine("down 8")
        self.assertEqual(self.test_day.horizontal_position, 13)
        self.assertEqual(self.test_day.depth, 10)

        self.test_day.move_submarine("forward 2")
        self.assertEqual(self.test_day.horizontal_position, 15)
        self.assertEqual(self.test_day.depth, 10)
        self.assertEqual(self.test_day.get_position_product(), 150)
