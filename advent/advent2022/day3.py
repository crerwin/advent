from advent.day import Day


class Day3(Day):
    year = 2022
    day = 3

    def _part1(self):
        return get_priorities_sum(self.input().splitlines())

    def _part2(self):
        return part2_priorities_sum(self.input().splitlines())


def split_line(line: str) -> tuple[str, str]:
    if len(line) % 2 != 0:
        raise ValueError(f"{line} does not have an even number of characters")
    else:
        line_midpoint = int(len(line) / 2)
        return line[0:line_midpoint], line[line_midpoint:]


def find_common_element(item_strings: list[str]) -> str:
    common_elements = set(item_strings[0])
    for item_string in item_strings:
        common_elements = common_elements.intersection(set(item_string))

    if len(common_elements) > 1:
        raise ValueError(
            f"Found more than one common character in input: {common_elements}"
        )
    else:
        common_str = ""
        for s in common_elements:
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
        item = find_common_element([rucksack_split[0], rucksack_split[1]])
        priorities_sum += get_item_priority(item)

    return priorities_sum


def part2_priorities_sum(items: list[str]) -> int:
    priorities_sum = 0

    if len(items) % 3 != 0:
        raise ValueError(
            f"List of items not groupable by three.  len(items): {len(items)}"
        )
    else:
        for i in range(0, len(items), 3):
            elf_group = items[i : i + 3]
            priorities_sum += get_item_priority(find_common_element(elf_group))

    return priorities_sum
