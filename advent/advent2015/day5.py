from advent.day import Day


class Day5(Day):
    year = 2015
    day = 5

    def _part1(self):
        return checklines(self.input())

    def _part2(self):
        return checklines(self.input(), "part2")


def textonly(inputfilename):
    file = open(inputfilename)
    content = file.read()
    result = checklines(content)
    result2 = checklines(content, "part2")
    return "Nice lines: " + str(result) + " part 2 Nice lines: " + str(result2)


def criteria1(input):
    vowels = ["a", "e", "i", "o", "u"]
    vowelcount = 0
    for char in input:
        if char in vowels:
            vowelcount += 1
    if vowelcount >= 3:
        return True
    else:
        return False


def criteria2(input):
    prevchar = ""
    for char in input:
        if char == prevchar:
            return True
        prevchar = char
    return False


def criteria3(input):
    badstrings = ["ab", "cd", "pq", "xy"]
    for badstring in badstrings:
        if badstring in input:
            return False
    return True


def criteria4(input):
    listofstringpairs = []
    for char1, char2 in zip(input[::1], input[1::1]):
        tempstring = char1 + char2
        if tempstring in listofstringpairs[0 : len(listofstringpairs) - 1]:
            return True
        else:
            listofstringpairs.append(tempstring)
    return False


def criteria5(input):
    for char1, char2, char3 in zip(input[::1], input[1::1], input[2::1]):
        if char1 == char3:
            return True
    return False


def isnice(input, part="part1"):
    if part == "part1":
        return criteria1(input) and criteria2(input) and criteria3(input)
    elif part == "part2":
        return criteria4(input) and criteria5(input)
    else:
        return False


def checklines(content, part="part1"):
    nicelines = 0
    for line in content.splitlines():
        if isnice(line, part):
            nicelines += 1
    return nicelines
