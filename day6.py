#module day6

class LightArray():
    def __init__(self):
        self.lights = [[False for i in range(1000)] for i in range(1000)]

    def turnon(self, x1, y1, x2, y2):
        for x in range(x1, x2):
            for y in range(y1, y2):
                self.lights[x],[y] = True

    def turnoff(self, x1, y1, x2, y2):
        for x in range(x1, x2):
            for y in range(y1, y2):
                self.lights[x],[y] = False

    def toggle(self, x1, y1, x2, y2):
        for x in range(x1, x2):
            for y in range (y1, y2):
                self.lights[x],[y] = not self.lights[x],[y]

    def get_lit_count(self):
        litcount = 0
        for x in range(0, 999):
            for y in range(0, 999):
                if self.lights[x][y] == True:
                    litcount += 1
        return litcount



def init():
    griswold = LightArray()


def textonly(inputfilename):
    file = open(inputfilename)
    content = file.read()
    for line in content.splitlines():
        print(parseline(line))


def parseline(input):
    words = input.split(" ")
    if len(words) == 4:
        operator = words[0]
        x1, y1 = words[1].split(",")
        x2, y2 = words[3].split(",")
    elif len(words) == 5:
        operator = words[1]
        x1, y1 = words[2].split(",")
        x2, y2 = words[4].split(",")
    else:
        raise ValueError('bad input line')
    return operator, x1, y1, x2, y2

