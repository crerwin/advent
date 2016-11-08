import os
import sys
from days import *

class Dispatcher():
    def exec_day(self, day_number):
        method_name = 'execday' + str(day_number)
        method = getattr(self, method_name, lambda: "not implemented")
        return method()

    def makefilepath(self, filename):
        return os.path.join('inputs', filename)

    def execday1(self):
        inputfilename = self.makefilepath("day1input.txt")
        return day1.textonly(inputfilename)

    def execday2(self):
        inputfilename = self.makefilepath("day2input.txt")
        return day2.textonly(inputfilename)

    def execday3(self):
        inputfilename = self.makefilepath("day3input.txt")
        return day3.textonly(inputfilename)

    def execday4(self):
        key = "ckczppom"
        return day4.textonly(key)

    def execday5(self):
        inputfilename = self.makefilepath("day5input.txt")
        return day5.textonly(inputfilename)

    def execday6(self):
        inputfilename = self.makefilepath("day6input.txt")
        return day6.textonly(inputfilename)

    def execday7(self):
        inputfilename = self.makefilepath("day7input.txt")
        return day7.textonly(inputfilename)

    def execday8(self):
        inputfilename = self.makefilepath("day8input.txt")
        return day8.textonly(inputfilename)

    def execday10(self):
        return len(day10.iterate("3113322113", 50))

    def execday11(self):
        pw = day11.password("vzbxkghb")
        pw.find_next_password()
        print(pw.get_password())
        pw.find_next_password()
        return pw.get_password()

    def execday12(self):
        myparser = day12.parser()

    def execday14(self):
        race = day14.OfficialRace()
        return race.run()


def main():
    if len(sys.argv) == 1:
        print("Must specify day")
    elif len(sys.argv) == 2:
        dispatcher = Dispatcher()
        print(dispatcher.exec_day(sys.argv[1]))
    else:
        print("too many arguments")


if __name__ == '__main__':
    sys.exit(main())
