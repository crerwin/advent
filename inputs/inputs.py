def get_input(year, day):
    if year == 2015 and day == 4:
        return "ckczppom"
    elif year == 2015 and day == 10:
        return "3113322113"
    else:
        f = open(f"inputs/{year}/day{day}input.txt")
        return f.read()
