# module day8


def parse_line(line):
    chars = len(line)
    print(line)
    special_count = 2
    encode_count = 2
    i = 0
    while i < chars:
        if line[i] == "\\":
            encode_count += 1
            if line[i + 1] == "x":
                special_count += 3
                i += 3
            else:
                encode_count += 1
                special_count += 1
                i += 1
        elif line[i] == "\"":
            encode_count += 1
        i += 1
    print(special_count, encode_count)
    return special_count, encode_count


def textonly(inputfilename):
    file = open(inputfilename)
    content = file.read()
    total = 0
    total_encode_chars = 0
    for line in content.splitlines():
        results = parse_line(line)
        total += results[0]
        total_encode_chars += results[1]
    return total, total_encode_chars
