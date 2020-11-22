import hashlib

from advent.day import Day


class Day4(Day):
    def __init__(self):
        super().__init__()
        self.year = 2015
        self.day = 4

    def part1(self):
        return findvalidhash(self.input())

    def part2(self):
        return findvalidhash(self.input(), 6)


def textonly(input):
    result5 = findvalidhash(input)
    result6 = findvalidhash(input, 6)
    stringresult = "Part 1: " + result5 + " Part 2: " + result6
    return stringresult


def hashvalue(key, value):
    input = key + value
    return hashlib.md5(input.encode("utf-8")).hexdigest()


def isvalidhash(myhash, numzeros=5):
    # we only define it as strings that start with 00000 because that's the challenge
    if numzeros == 5:
        target = "00000"
    elif numzeros == 6:
        target = "000000"
    else:
        raise ValueError("only 5 and 6 are acceptable here")
    if myhash[:numzeros] == target:
        return True
    else:
        return False


def findvalidhash(key, numzeros=5):
    # we should multithread!
    for i in range(1, 100000000):
        if isvalidhash(hashvalue(key, str(i)), numzeros):
            return str(i)
    return 0
