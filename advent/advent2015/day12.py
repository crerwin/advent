from advent.day import Day


class Day12(Day):
    year = 2015
    day = 12

    def _part1(self):
        return part_a(self.input())


def part_a(contents):
    ints = []
    for s in contents.split():
        if s.isdigit():
            ints.append(int(s))
    # ints = int(num) for num in contents.split() if s.isdigit()
    total = sum(ints)
    return total
