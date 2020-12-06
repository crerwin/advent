from advent.day import Day


class Day2(Day):
    year = 2020
    day = 2

    def _part1(self):
        return count_valid(self.input().splitlines())

    def _part2(self):
        return count_valid_2(self.input().splitlines())


def count_valid(inputs: [str]) -> int:
    count = 0
    for line in inputs:
        if is_valid(line):
            count += 1
    return count


def count_valid_2(inputs: [str]) -> int:
    count = 0
    for line in inputs:
        if is_valid_2(line):
            count += 1
    return count


def is_valid(input: str) -> bool:
    req_char = get_required_char(input)
    password = get_password(input)
    min_count = get_min(input)
    max_count = get_max(input)
    count = password.count(req_char)
    return count >= min_count and count <= max_count


def is_valid_2(input: str) -> bool:
    req_char = get_required_char(input)
    password = get_password(input)
    first_pos = get_min(input)
    second_pos = get_max(input)
    count = 0
    if password[first_pos - 1] == req_char:
        count += 1
    if password[second_pos - 1] == req_char:
        count += 1
    return count == 1

    return False


def get_min(input: str) -> int:
    min = input.split("-")[0]
    return int(min)


def get_max(input: str) -> int:
    chunks = input.split()
    max = chunks[0].split("-")[1]
    return int(max)


def get_required_char(input: str) -> str:
    chunks = input.split()
    req_char = chunks[1][:-1]
    return req_char


def get_password(input: str) -> str:
    chunks = input.split()
    return chunks[-1]
