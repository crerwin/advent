inputs = {
    2015: {
        4: "ckczppom",
        10: "3113322113",
        11: "vzbxkghb"
    }
}


def get_input(year, day):
    if year in inputs and day in inputs[year]:
        return inputs[year][day]
    else:
        f = open(f"inputs/{year}/day{day}input.txt")
        return f.read()
