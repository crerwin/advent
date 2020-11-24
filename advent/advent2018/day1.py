from advent.day import Day


class Day1(Day):
    year = 2018
    day = 1

    def _part1(self):
        return walk(0, input_to_list(self.input()))

    def _part2(self):
        return find_repeated_frequency(0, input_to_list(self.input()))


def input_to_list(input):
    return input.splitlines()


def step(location, instruction):
    sign = instruction[0]
    value = int(instruction[1:])
    if sign == "+":
        location += value
    else:
        location -= value
    return location


def walk(start, input):
    location = start
    for instruction in input:
        location = step(location, instruction)
    return location


def find_repeated_frequency(start, input):
    location = start
    visited_locations = []
    i = 0
    while location not in visited_locations:
        visited_locations.append(location)
        location = step(location, input[i])
        if i >= len(input) - 1:
            i = 0
        else:
            i += 1
    return location
