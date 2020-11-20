from advent.day import Day


class Day3(Day):
    def __init__(self):
        super().__init__()
        self.year = 2015
        self.day = 3

    def part1(self):
        return str(walk(self.input(), "part1"))

    def part2(self):
        return str(walk(self.input(), "part2"))


class Coordinates:
    x = 0
    y = 0


class Person:
    def __init__(self):
        self.coords = Coordinates()
        self.coords.x = 0
        self.coords.y = 0

    def moveup(self):
        self.coords.y += 1

    def movedown(self):
        self.coords.y -= 1

    def moveright(self):
        self.coords.x += 1

    def moveleft(self):
        self.coords.x -= 1


class Dispatcher(Person):
    # dispatcher is a class that 'impersonates' a person.  It keeps track of who is moving (Santa or RoboSanta)
    # and coords is masked so that when the calling function asks, it gets the correct set of coords
    # this assumes coords is asked for after moving.  Changing that would require refactoring.

    def __init__(self):
        self.santa = Person()
        self.robo_santa = Person()
        self.nexttomove = self.santa
        self.lasttomove = self.robo_santa

    def moveup(self):
        self.nexttomove.moveup()
        self.switchnexttomove()

    def movedown(self):
        self.nexttomove.movedown()
        self.switchnexttomove()

    def moveright(self):
        self.nexttomove.moveright()
        self.switchnexttomove()

    def moveleft(self):
        self.nexttomove.moveleft()
        self.switchnexttomove()

    def _get_coords(self):
        return self.lasttomove.coords

    def switchnexttomove(self):
        # there's probably a better way to do this
        if self.nexttomove == self.santa:
            self.nexttomove = self.robo_santa
            self.lasttomove = self.santa
        elif self.nexttomove == self.robo_santa:
            self.nexttomove = self.santa
            self.lasttomove = self.robo_santa
        else:
            raise Exception("nexttomove is assigned to an impossible value?!")

    coords = property(_get_coords)


def textonly(inputfilename):
    file = open(inputfilename)
    content = file.read()
    santaresult = walk(content, "part1")
    bothresult = walk(content, "part2")
    stringresult = (
        "Number of houses visited by Santa only: "
        + str(santaresult)
        + " number of houses visited by Both: "
        + str(bothresult)
    )
    return stringresult


def walk(content, part="part1"):
    if not content:
        # string is empty
        return 0
    else:
        Santa = getpersontype(part)
        visitedhousesdict = {(Santa.coords.x, Santa.coords.y): 1}
        for char in content:
            try:
                moveperson(Santa, char)
                # maybe defaultdict is better here?
                if (Santa.coords.x, Santa.coords.y) in visitedhousesdict:
                    # have we been to this house?  then increment
                    visitedhousesdict[(Santa.coords.x, Santa.coords.y)] += 1
                else:
                    # add a newly visited house to the list
                    visitedhousesdict[(Santa.coords.x, Santa.coords.y)] = 1
            except ValueError:
                raise
    return len(visitedhousesdict)


def getpersontype(part):
    if part == "part1":
        return Person()
    elif part == "part2":
        return Dispatcher()
    else:
        raise ValueError("bad value for part")


def moveperson(person, char):
    if char == ">":
        person.moveright()
    elif char == "<":
        person.moveleft()
    elif char == "^":
        person.moveup()
    elif char == "v":
        person.movedown()
    else:
        raise ValueError(f"bad character found: {char}")
