from advent.day import Day

# migrated from:
# https://github.com/crerwin/advent2017/blob/master/advent2017/day1.py


class Day1(Day):
    year = 2017
    day = 1

    def _part1(self):
        return process_captcha(self.input())

    def _part2(self):
        return process_captcha_2(self.input())


def process_captcha(captcha):
    sum = 0
    for i in range(len(captcha)):
        if i == len(captcha) - 1:
            next = 0
        else:
            next = i + 1
        if captcha[i] == captcha[next]:
            sum += int(captcha[i])
    return sum


def process_captcha_2(captcha):
    sum = 0
    for i in range(len(captcha)):
        if i >= len(captcha) / 2:
            compare = i - int(len(captcha) / 2)
        else:
            compare = i + int(len(captcha) / 2)
        if captcha[i] == captcha[compare]:
            sum += int(captcha[i])
    return sum
