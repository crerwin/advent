from advent.day import Day


class Day1(Day):
    year = 2020
    day = 1

    def _part1(self):
        return get_prod(self.input().splitlines())

    def _part2(self):
        return get_prod_2(self.input().splitlines())


def get_prod(inputs):
    for i in range(len(inputs)):
        for j in range(i, len(inputs)):
            x = int(inputs[i])
            y = int(inputs[j])
            if x + y == 2020:
                return x * y


def get_prod_2(inputs):
    for i in range(len(inputs)):
        for j in range(i, len(inputs)):
            for k in range(j, len(inputs)):
                x = int(inputs[i])
                y = int(inputs[j])
                z = int(inputs[k])
                if x + y + z == 2020:
                    return x * y * z
