#module day5


def textonly(inputfilename):
    file = open(inputfilename)
    content = file.read()
    result = checklines(content)
    return "Nice lines: " + str(result)

def criteria1(input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelcount = 0
    for char in input:
        if char in vowels:
            vowelcount += 1
    if vowelcount >= 3:
        return True
    else:
        return False


def criteria2(input):
    prevchar = ''
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


def isnice(input):
    return criteria1(input) and criteria2(input) and criteria3(input)


def checklines(content):
    nicelines = 0
    for line in content.splitlines():
        if isnice(line):
            nicelines += 1
    return nicelines

