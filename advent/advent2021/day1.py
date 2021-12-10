from advent.day import Day


class Day1(Day):
    year = 2021
    day = 1

    def _part1(self):
        return count_depth_increases(self.input().splitlines())

    def _part2(self):
        return super()._part2()


def count_depth_increases(inputs):
    count = 0
    previous_measurement = None
    for measurement in inputs:
        measurement = int(measurement)
        if previous_measurement and previous_measurement < measurement:
            count += 1
        previous_measurement = measurement
    return count
