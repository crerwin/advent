from advent.day import Day


class Day1(Day):
    year = 2021
    day = 1

    def _part1(self):
        return count_depth_increases(self.input().splitlines())

    def _part2(self):
        return sliding_window_increases(self.input().splitlines())


def count_depth_increases(inputs):
    count = 0
    previous_measurement = None
    for measurement in inputs:
        measurement = int(measurement)
        if previous_measurement and previous_measurement < measurement:
            count += 1
        previous_measurement = measurement
    return count


def sliding_window_increases(inputs):
    count = 0
    previous_measurements = [None, None, None]
    for measurement in inputs:
        measurement = int(measurement)
        if (
            previous_measurements[0]
            and previous_measurements[1]
            and previous_measurements[2]
        ):
            previous_window_sum = (
                previous_measurements[0]
                + previous_measurements[1]
                + previous_measurements[2]
            )
            current_window_sum = (
                measurement + previous_measurements[0] + previous_measurements[1]
            )
            if current_window_sum > previous_window_sum:
                count += 1
        previous_measurements[2] = previous_measurements[1]
        previous_measurements[1] = previous_measurements[0]
        previous_measurements[0] = measurement

    return count
