from advent.day import Day


class Day2(Day):
    year = 2018
    day = 2

    def part1(self):
        return str(get_checksum(input_to_list(self.input())))

    def part2(self):
        return get_correct_id_common(input_to_list(self.input()))


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


def get_common_chars(str1: str, str2: str) -> str:
    if len(str1) != len(str2):
        raise ValueError("String lengths do not match.")

    common_str = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            common_str += str1[i]

    return common_str


def get_correct_id_common(input):
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            comm_chars = get_common_chars(input[i], input[j])
            if len(comm_chars) == (len(input[i]) - 1):
                return comm_chars
