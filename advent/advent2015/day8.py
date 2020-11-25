from advent.day import Day


class Day8(Day):
    year = 2015
    day = 8

    def _part1(self):
        return textonly(self.input())[0]

    def _part2(self):
        return textonly(self.input())[1]


def parse_line(line):
    chars = len(line)
    special_count = 2
    encode_count = 2
    i = 0
    while i < chars:
        if line[i] == "\\":
            encode_count += 1
            if line[i + 1] == "x":
                special_count += 3
                i += 3
            else:
                encode_count += 1
                special_count += 1
                i += 1
        elif line[i] == '"':
            encode_count += 1
        i += 1
    return special_count, encode_count


def textonly(content):
    total = 0
    total_encode_chars = 0
    for line in content.splitlines():
        results = parse_line(line)
        total += results[0]
        total_encode_chars += results[1]
    return total, total_encode_chars
