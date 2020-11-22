from advent.day import Day


class Day2(Day):
    def __init__(self):
        super().__init__()
        self.year = 2018
        self.day = 2

    def part1(self):
        return get_checksum(input_to_list(self.input()))

    def part2(self):
        return None


def input_to_list(input):
    return input.splitlines()


def exactly_two_of_any_letter(input):
    for char in input:
        if input.count(char) == 2:
            return True
    return False


def exactly_three_of_any_letter(input):
    for char in input:
        if input.count(char) == 3:
            return True
    return False


def get_checksum(input):
    exactly_two = 0
    exactly_three = 0
    for line in input:
        if exactly_two_of_any_letter(line):
            exactly_two += 1
        if exactly_three_of_any_letter(line):
            exactly_three += 1
    return exactly_two * exactly_three
