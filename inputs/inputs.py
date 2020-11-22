def get_input(year, day):
    if year == 2015 and day == 4:
        return "ckczppom"
    else:
        f = open(f"inputs/{year}/day{day}input.txt")
        return f.read()
