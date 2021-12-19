from typing import ValuesView
from advent.day import Day


class Day2(Day):
    year = 2021
    day = 2
    horizontal_position = 0
    depth = 0
    aim = 0

    def _part1(self):
        self.follow_instructions(self.input().splitlines())
        return self.get_position_product()

    def _part2(self):
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0
        self.follow_instructions(self.input().splitlines(), part=2)
        return self.get_position_product()

    def valid_instruction(self, instruction):
        valid_directions = ["forward", "down", "up"]
        instruction_split = instruction.split()
        direction = instruction_split[0]
        amount = instruction_split[1]
        if len(instruction_split) != 2:
            return False
        if direction not in valid_directions:
            return False
        if not amount.isdigit():
            return False
        return True

    def move_submarine(self, instruction, part=1):
        if self.valid_instruction(instruction):
            direction, amount = instruction.split()
            amount = int(amount)
            if part == 1:
                if direction == "forward":
                    self.horizontal_position += amount
                elif direction == "down":
                    self.depth += amount
                elif direction == "up":
                    self.depth -= amount
                else:
                    raise (ValueError)
            elif part == 2:
                if direction == "down":
                    self.aim += amount
                elif direction == "up":
                    self.aim -= amount
                elif direction == "forward":
                    self.horizontal_position += amount
                    self.depth += self.aim * amount
                else:
                    raise (ValueError)
            else:
                raise (ValueError)
        else:
            raise (ValueError)

    def follow_instructions(self, instructions, part=1):
        for instruction in instructions:
            self.move_submarine(instruction, part)

    def get_position_product(self):
        return self.horizontal_position * self.depth
