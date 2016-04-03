#module day10


def lookAndSay(input):
    result = ""
    last_char = "A"
    repeat_count = 1
    for char in input:
        if char == last_char:
            repeat_count += 1
        else:
            if last_char != "A":
                result += str(repeat_count)
                result += last_char
            last_char = char
            repeat_count = 1
    result += str(repeat_count)
    result += last_char
    return result

def iterate(input, num_iterations):
    result = input
    for i in range(0,num_iterations):
        result = lookAndSay(result)
    return result
        
