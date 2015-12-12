#module day2.py

def textonly(inputfilename):
    file = open(inputfilename)
    content = file.read()
    result = calc(content)
    stringresult = "Paper area: " + str(result['paperarea']) + " ribbon length: " + str(result['ribbonlength'])
    return stringresult

def calc(content):
    area = 0
    ribbonlength = 0
    for line in content.splitlines():
        if "x" in line:
            length, width, height = (int(n) for n in line.split('x'))
            area += wrap(length, width, height)
            ribbonlength += ribbon(length, width, height)
    return {'paperarea':area, 'ribbonlength':ribbonlength}

def wrap(length, width, height):
    side1 = length * width
    side2 = width * height
    side3 = length * height
    extra = min(side1, side2, side3)
    return 2 * side1 + 2 * side2 + 2 * side3 + extra

def ribbon(length, width, height):
    smallestdimension, nextsmallestdimension, largestdimension = sorted([length, width, height])
    return 2 * smallestdimension + 2 * nextsmallestdimension + length * width * height