#module day6


class LightArray():
    def __init__(self):
        self.lights = [[False for i in range(1000)] for i in range(1000)]

    def turnon(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights[x][y] = True

    def turnoff(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights[x][y] = False

    def toggle(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range (y1, y2 + 1):
                self.lights[x][y] = not self.lights[x][y]

    def act(self, operator, x1, y1, x2, y2):
        if operator == "off":
            self.turnoff(x1, y1, x2, y2)
        elif operator == "on":
            self.turnon(x1, y1, x2, y2)
        elif operator == "toggle":
            self.toggle(x1, y1, x2, y2)
        else:
            raise ValueError('bad value for operator')

    def get_lit_count(self):
        litcount = 0
        for x in range(0, 1000):
            for y in range(0, 1000):
                if self.lights[x][y]:
                    litcount += 1
        return litcount


class Part2Array(LightArray):
    def __init__(self):
        self.brightness = 0
        self.lights = [[0 for i in range(1000)] for i in range(1000)]

    def turnon(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights[x][y] +=1

    def turnoff(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if self.lights[x][y] > 0:
                    self.lights[x][y] -= 1

    def toggle(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range (y1, y2 + 1):
                self.lights[x][y] += 2

    def get_brightness(self):
        brightness = 0
        for x in range(0, 1000):
            for y in range(0, 1000):
                brightness += self.lights[x][y]
        return brightness


def textonly(inputfilename):
    griswold = LightArray()
    griswold2 = Part2Array()
    file = open(inputfilename)
    content = file.read()
    for line in content.splitlines():
        result = parseline(line)
        griswold.act(*result)
    for line in content.splitlines():
        result = parseline(line)
        griswold2.act(*result)
    stringresult = "Lights lit (part 1): " + str(griswold.get_lit_count()) + " Brightness (part 2): " + str(griswold2.get_brightness())
    return stringresult


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
    return operator, int(x1), int(y1), int(x2), int(y2)

