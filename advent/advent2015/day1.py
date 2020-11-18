from advent.day import Day


class Day1(Day):
    def __init__(self, inputfilename):
        f = open(inputfilename)
        self.input_data = f.read()

    def part1(self):
        result = self.walk()
        stringresult = (
            "Final floor: "
            + str(result["floor"])
            + " Basement entry character: "
            + str(result["basementchar"])
        )
        return stringresult

    def walk(self):
        floor = 0
        max = 0
        min = 0
        basementchar = 0
        count = 0
        for char in self.input_data:
            count += 1
            if char == "(":
                floor += 1
            else:
                floor -= 1
            if floor > max:
                max = floor
            if floor < min:
                min = floor
            if floor < 0 and basementchar == 0:
                basementchar = count
        return {"floor": floor, "basementchar": basementchar}
