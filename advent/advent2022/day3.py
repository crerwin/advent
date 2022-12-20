from advent.day import Day


class Day3(Day):
    year = 2022
    day = 3

    def _part1(self):
        return get_priorities_sum(self.input().splitlines())


def split_line(line: str) -> tuple[str, str]:
    if len(line) % 2 != 0:
        raise ValueError(f"{line} does not have an even number of characters")
    else:
        line_midpoint = int(len(line) / 2)
        return line[0:line_midpoint], line[line_midpoint:]


def find_common_element(string1: str, string2: str) -> str:
    if len(string1) != len(string2):
        raise ValueError(f"Length of {string1} not equal to length of {string2}")
    else:
        common_set = set(string1) & set(string2)
        if len(common_set) > 1:
            raise ValueError(
                f"Found more than one common character in {string1} & {string2}: {common_set}"
            )
        else:
            common_str = ""
            for s in common_set:
                common_str = common_str + s

            return common_str


def get_item_priority(item: str) -> int:
    if len(item) > 1:
        raise ValueError(f"Invalid item received: {item}")

    # if lowercase
    elif item == item.lower():
        return ord(item) - 96
    # assume uppercase (could use more safety but meh)
    else:
        return ord(item) - 38


def get_priorities_sum(items: list[str]) -> int:
    priorities_sum = 0
    for rucksack in items:
        rucksack_split = split_line(rucksack)
        item = find_common_element(rucksack_split[0], rucksack_split[1])
        priorities_sum += get_item_priority(item)

    return priorities_sum
