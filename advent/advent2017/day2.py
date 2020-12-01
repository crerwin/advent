from advent.day import Day


class Day2(Day):
    year = 2017
    day = 2

    def _part1(self):
        return checksum(self.input())

    def _part2(self):
        return checksum2(self.input())


def row_to_ints(row):
    rowlist = row.split()
    return list(map(int, rowlist))


def checksum(sheet):
    lines = sheet.splitlines()
    checksum = 0
    for line in lines:
        row = row_to_ints(line)
        checksum += checksum_row(row)
    return checksum


def checksum2(sheet):
    lines = sheet.splitlines()
    checksum = 0
    for line in lines:
        row = row_to_ints(line)
        checksum += checksum_row2(row)
    return checksum


def checksum_row(row):
    if len(row) == 0:
        return 0
    min = row[0]
    max = row[0]
    for n in row:
        if n < min:
            min = n
        if n > max:
            max = n
    return max - min


def checksum_row2(row):
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[i] < row[j]:
                if row[j] % row[i] == 0:
                    return int(row[j] / row[i])
            if row[i] % row[j] == 0:
                return int(row[i] / row[j])

    return 0
