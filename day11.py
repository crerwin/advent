#module day11

class password():
    def __init__(self, password_value):
        if len(password_value) == 8:
            self.password_value = password_value.lowercase
        else:
            raise ValueError("wrong length password")


    def increment_character(self, input):
        return chr(ord(input) + 1)

    #def increment_password(self):




    def meets_requirement_1(self):
        prev_char = ""
        run_count = 1
        for char in self.password_value:
            if prev_char != "":
                if self.increment_character(prev_char) == char:
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
        if not self.meets_requirement_1(): #this is the fastest check
            return False
        if not self.meets_requirement_2():
            return False
        if not self.meets_requirement_3():
            return False
        return True

