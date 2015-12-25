import os
import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8


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


def execday6():
    inputfilename = makefilepath("day6input.txt")
    print(day6.textonly(inputfilename))

def execday7():
    inputfilename = makefilepath("day7input.txt")
    print(day7.textonly(inputfilename))

def execday8():
    inputfilename = makefilepath("day8input.txt")
    print(day8.textonly(inputfilename))

execday8()
