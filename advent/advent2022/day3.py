from advent.day import Day


class Day3(Day):
    year = 2022
    day = 3


def split_line(line: str) -> tuple[str, str]:
    print(len(line))
    if len(line) % 2 != 0:
        raise ValueError(f"{line} does not have an even number of characters")
    else:
        return line[0:2], line[2:]


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
            if len(common_str) > 1:
                raise ValueError(
                    f"Found more than one common character in {string1} & {string2}: {common_set}"
                )
            else:
                return common_str
