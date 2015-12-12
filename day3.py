#module day3.py


class Coordinates():
    x = 0
    y = 0


class Person():
    coords = Coordinates()

    def __init__(self):
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


def textonly(inputfilename):
    file = open(inputfilename)
    content = file.read()
    result = walk(content)
    stringresult = "Number of houses visited: " + str(result)
    return stringresult


def walk(content):
    if not content:
        # string is empty
        return 0
    else:
        Santa = Person()
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
        raise ValueError('bad character found')
