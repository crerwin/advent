from advent.day import Day


class Day3(Day):
    year = 2020
    day = 3

    slope = []

    def _part1(self):
        self.load_slope(self.input().splitlines())
        return self.ski(3, 1)

    def _part2(self):
        self.load_slope(self.input().splitlines())
        checksum = self.ski(1, 1)
        checksum *= self.ski(3, 1)
        checksum *= self.ski(5, 1)
        checksum *= self.ski(7, 1)
        checksum *= self.ski(1, 2)
        return checksum

    def load_slope(self, input: [str]):
        self.slope = []
        for line in input:
            slope_line = []
            for char in line:
                slope_line.append(char)
            self.slope.append(slope_line)

    def ski(self, right: int, down: int):
        position = 0
        trees = 0
        for row in range(0, len(self.slope), down):
            if self.slope[row][position] == "#":
                trees += 1
            position += right
            if position >= len(self.slope[row]):
                position = position - len(self.slope[row])
        return trees
