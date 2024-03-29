from inputs import inputs


class Day(object):
    # All days implement Day, so if a given day has not implemented
    # a specific part, it will return the defaults below.
    input_data = None
    year = None
    day = None

    def input(self):
        if not self.input_data:
            self.input_data = inputs.get_input(self.year, self.day)
        return self.input_data

    def part(self, part_num):
        if part_num == 1:
            return self.part1()
        elif part_num == 2:
            return self.part2()
        else:
            return "invalid part number specified - only 1 and 2 are valid."

    def part1(self):
        return str(self._part1())

    def part2(self):
        return str(self._part2())

    def _part1(self):
        return f"Advent {self.year} Day {self.day} part 1 not yet implemented."

    def _part2(self):
        return f"Advent {self.year} Day {self.day} part 2 not yet implemented."
