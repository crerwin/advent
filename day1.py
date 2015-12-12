#module day1.py

def textonly(inputfilename):
    file = open(inputfilename)
    content = file.read()
    result = walk(content)
    stringresult = "Final floor: " + str(result['floor']) + " Basement entry character: " + str(result['basementchar'])
    return stringresult

def walk(content):
    floor = 0
    max = 0
    min = 0
    basementchar = 0
    count = 0
    for char in content:
        count += 1
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor > max:
            max = floor
        if floor < min:
            min = floor
        if floor < 0 and basementchar == 0:
            basementchar = count
    return {'floor':floor,'basementchar':basementchar}
