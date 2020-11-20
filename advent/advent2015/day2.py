from advent.day import Day


class Day2(Day):
    def __init__(self):
        super().__init__()
        self.year = 2015
        self.day = 2

    def part1(self):
        result = calc(self.input())
        return str(result["paperarea"])

    def part2(self):
        result = calc(self.input())
        return str(result["ribbonlength"])


def calc(content):
    area = 0
    ribbonlength = 0
    for line in content.splitlines():
        if "x" in line:
            length, width, height = (int(n) for n in line.split("x"))
            area += wrap(length, width, height)
            ribbonlength += ribbon(length, width, height)
    return {"paperarea": area, "ribbonlength": ribbonlength}


def wrap(length, width, height):
    side1 = length * width
    side2 = width * height
    side3 = length * height
    extra = min(side1, side2, side3)
    return 2 * side1 + 2 * side2 + 2 * side3 + extra


def ribbon(length, width, height):
    smallestdimension, nextsmallestdimension, largestdimension = sorted(
        [length, width, height]
    )
    return 2 * smallestdimension + 2 * nextsmallestdimension + length * width * height
