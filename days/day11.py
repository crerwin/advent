# module day11


class password():
    def __init__(self, password_value):
        if len(password_value) == 8:
            self.password_value = password_value.lower()
        else:
            raise ValueError("wrong length password")

    def get_password(self):
        return self.password_value

    def increment_character(self, input):
        if input == "z":
            return "a"
        else:
            return chr(ord(input) + 1)

    def increment_password(self):
        if self.password_value == "zzzzzzzz":
            self.password_value = "aaaaaaaa"
        else:
            templist = list(self.password_value)
            for currchar in range(len(templist) - 1, 0, -1):
                tempchar = self.increment_character(chr(ord(self.password_value[currchar])))
                if tempchar != "a":
                    templist[currchar] = tempchar
                    break
                else:
                    templist[currchar] = tempchar
            self.password_value = ''.join(templist)

    def find_next_password(self):
        self.increment_password()
        while not self.is_valid():
            self.increment_password()


    def meets_requirement_1(self):
        prev_char = ""
        run_count = 1
        for char in self.password_value:
            if prev_char != "":
                if self.increment_character(prev_char) == char and prev_char != "z":
                    run_count += 1
                else:
                    run_count = 1
            if run_count >= 3:
                return True
            prev_char = char
        return False

    def meets_requirement_2(self):
        if "i" in self.password_value:
            return False
        if "o" in self.password_value:
            return False
        if "l" in self.password_value:
            return False
        return True

    def meets_requirement_3(self):
        prevchar = ""
        paircount = 0
        for char in self.password_value:
            if char == prevchar:
                paircount += 1
                prevchar = ""
            else:
                prevchar = char
        if paircount >= 2:
            return True
        else:
            return False

    def is_valid(self):
        if not self.meets_requirement_1():  # this is the fastest check
            return False
        if not self.meets_requirement_2():
            return False
        if not self.meets_requirement_3():
            return False
        return True
