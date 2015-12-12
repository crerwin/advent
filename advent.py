import os
import day1
import day2
import day3
import day4
import day5


def makefilepath(filename):
    return os.path.join('inputs', filename)


def execday1():
    inputfilename = makefilepath("day1input.txt")
    print(day1.textonly(inputfilename))


def execday2():
    inputfilename = makefilepath("day2input.txt")
    print(day2.textonly(inputfilename))


def execday3():
    inputfilename = makefilepath("day3input.txt")
    print(day3.textonly(inputfilename))


def execday4():
    key = "ckczppom"
    print(day4.textonly(key))


def execday5():
    inputfilename = makefilepath("day5input.txt")
    print(day5.textonly(inputfilename))

execday5()
