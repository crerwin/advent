from advent.day import Day


class Day10(Day):
    year = 2015
    day = 10

    def _part1(self):
        return len(iterate(self.input(), 40))

    def _part2(self):
        return len(iterate(self.input(), 50))


def lookAndSay(input):
    result = ""
    last_char = "A"
    repeat_count = 1
    for char in input:
        if char == last_char:
            repeat_count += 1
        else:
            if last_char != "A":
                result += str(repeat_count)
                result += last_char
            last_char = char
            repeat_count = 1
    result += str(repeat_count)
    result += last_char
    return result


def iterate(input, num_iterations):
    result = input
    for i in range(0, num_iterations):
        result = lookAndSay(result)
    return result
