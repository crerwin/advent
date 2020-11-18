class Day(object):
    # All days implement Day, so if a given day has not implemented
    # a specific part, it will return the defaults below.
    def __init__(self):
        self.input_data = ""

    def part(self, part_num):
        if part_num == 1:
            return self.part1()
        elif part_num == 2:
            return self.part2()
        else:
            return "invalid part number specified - only 1 and 2 are valid."

    def part1(self):
        return "not yet implemented"

    def part2(self):
        return "not yet implemented"
