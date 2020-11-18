from advent.day import Day


class Day1(Day):
    def __init__(self, inputfilename):
        f = open(inputfilename)
        self.input_data = f.read()

    def part1(self):
        result = walk(self.input_data)
        return result["floor"]

    def part2(self):
        result = walk(self.input_data)
        return result["basementchar"]


def walk(instructions):
    floor = 0
    max = 0
    min = 0
    basementchar = 0
    count = 0
    for char in instructions:
        count += 1
        if char == "(":
            floor += 1
        else:
            floor -= 1
        if floor > max:
            max = floor
        if floor < min:
            min = floor
        if floor < 0 and basementchar == 0:
            basementchar = count
    return {"floor": floor, "basementchar": basementchar}
