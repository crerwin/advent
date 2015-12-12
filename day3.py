#module day3.py


class Coordinates():
    x = 0
    y = 0


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
        coords = Coordinates()
        visitedhousesdict = {(coords.x, coords.y): 1}
        for char in content:
            try:
                coords = adjustcoords(coords, char)
                # maybe defaultdict is better here?
                if (coords.x, coords.y) in visitedhousesdict:
                    # have we been to this house?  then increment
                    visitedhousesdict[(coords.x, coords.y)] += 1
                else:
                    # add a newly visited house to the list
                    visitedhousesdict[(coords.x, coords.y)] = 1
            except ValueError:
                raise
    return len(visitedhousesdict)


def adjustcoords(coords, char):
    if char == ">":
        coords.x += 1
    elif char == "<":
        coords.x -= 1
    elif char == "^":
        coords.y += 1
    elif char == "v":
        coords.y -= 1
    else:
        raise ValueError('bad character found')
    return coords
