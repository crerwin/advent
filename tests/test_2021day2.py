import unittest
import pytest
from .test_day import DayTest
from advent.advent2021 import day2


class TestDayFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.test_day = day2.Day2()
        self.test_instructions = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2",
        ]

    def test_valid_instruction(self):
        for instruction in self.test_instructions:
            self.assertTrue(self.test_day.valid_instruction(instruction))

        self.assertFalse(self.test_day.valid_instruction("forward 5 hi"))
        self.assertFalse(self.test_day.valid_instruction("back 3"))
        self.assertFalse(self.test_day.valid_instruction("3 3"))
        self.assertFalse(self.test_day.valid_instruction("forward hi"))
        self.assertFalse(self.test_day.valid_instruction("forward three"))

    def test_move_submarine_part_1(self):
        expected_positions = [(5, 0), (5, 5), (13, 5), (13, 2), (13, 10), (15, 10)]
        instruction_count = 0
        for instruction in self.test_instructions:
            self.test_day.move_submarine(instruction)
            self.assertEqual(
                self.test_day.horizontal_position,
                expected_positions[instruction_count][0],
            )
            self.assertEqual(
                self.test_day.depth, expected_positions[instruction_count][1]
            )
            instruction_count += 1
        self.assertEqual(self.test_day.get_position_product(), 150)

    def test_move_submarine_part_2(self):
        expected_positions = [
            (5, 0, 0),
            (5, 0, 5),
            (13, 40, 5),
            (13, 40, 2),
            (13, 40, 10),
            (15, 60, 10),
        ]
        instruction_count = 0
        for instruction in self.test_instructions:
            self.test_day.move_submarine(instruction, part=2)
            self.assertEqual(
                self.test_day.horizontal_position,
                expected_positions[instruction_count][0],
            )
            self.assertEqual(
                self.test_day.depth, expected_positions[instruction_count][1]
            )
            self.assertEqual(
                self.test_day.aim, expected_positions[instruction_count][2]
            )
            instruction_count += 1
        self.assertEqual(self.test_day.get_position_product(), 900)


@pytest.mark.day
class TestDay1(DayTest):
    test_day = day2.Day2()
    expected_part_1 = "1561344"
    expected_part_2 = "1848454425"
