from advent.day import Day


class Day1(Day):
    year = 2023
    day = 1

    def _part1(self):
        return self._get_calibration_sum(self.input().splitlines())

    def _get_calibration_sum(self, lines: [str]) -> int:
        if len(lines) < 1:
            raise ValueError(f"No lines were passed: {lines}")

        else:
            sum = 0
            for line in lines:
                sum += self._get_calibration_values(line)
            return sum

    def _get_calibration_values(self, line: str) -> int:
        return int(
            self._get_calibration_digit(line) + self._get_calibration_digit(line, True)
        )

    def _get_calibration_digit(self, line: str, reverse: bool = False) -> str:
        chars = list(line)

        if reverse:
            for char in chars[::-1]:
                if char.isdigit():
                    return char

        else:
            for char in chars:
                if char.isdigit():
                    return char

        raise ValueError(f"Did not find a digit in line: {line}")
