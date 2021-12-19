from typing import ValuesView
from advent.day import Day


class Day2(Day):
    year = 2021
    day = 2
    horizontal_position = 0
    depth = 0

    def _part1(self):
        self.follow_instructions(self.input().splitlines())
        return self.get_position_product()

    def _part2(self):
        return super()._part2()

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

    def move_submarine(self, instruction):
        if self.valid_instruction(instruction):
            direction, amount = instruction.split()
            if direction == "forward":
                self.horizontal_position += int(amount)
            elif direction == "down":
                self.depth += int(amount)
            elif direction == "up":
                self.depth -= int(amount)
            else:
                raise (ValueError)
        else:
            raise (ValueError)

    def follow_instructions(self, instructions):
        for instruction in instructions:
            self.move_submarine(instruction)

    def get_position_product(self):
        return self.horizontal_position * self.depth
