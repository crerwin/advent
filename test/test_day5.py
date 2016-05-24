import unittest
from days import day5


class Criteria1Case(unittest.TestCase):
    def test_criteria1_case_1(self):
        self.assertEquals(day5.criteria1("a"), False)

    def test_criteria1_case_2(self):
        self.assertEquals(day5.criteria1("aaa"), True)

    def test_criteria1_case_3(self):
        self.assertEquals(day5.criteria1("aei"), True)

    def test_criteria1_case_4(self):
        self.assertEquals(day5.criteria1("xazegov"), True)

    def test_criteria1_case_5(self):
        self.assertEquals(day5.criteria1("aeiouaeiouaeiou"), True)

    def test_criteria1_case_6(self):
        self.assertEquals(day5.criteria1("dvszwmarrgswjxmb"), False)


class Criteria2Case(unittest.TestCase):
    def test_criteria2_case_1(self):
        self.assertEquals(day5.criteria2("xx"), True)

    def test_criteria2_case_2(self):
        self.assertEquals(day5.criteria2("xy"), False)

    def test_criteria2_case_3(self):
        self.assertEquals(day5.criteria2("abcdde"), True)

    def test_criteria2_case_4(self):
        self.assertEquals(day5.criteria2("aabbccdd"), True)


class Criteria3Case(unittest.TestCase):
    def test_criteria3_case_1(self):
        self.assertEquals(day5.criteria3("haegwjzuvuyypxyu"), False)

    def test_criteria3_case_2(self):
        self.assertEquals(day5.criteria3("jchzalrnumimnmhp"), True)


class IsNiceCase(unittest.TestCase):
    def test_isnice_case_1(self):
        self.assertEquals(day5.isnice("aaa"), True)

    def test_isnice_case_2(self):
        self.assertEquals(day5.isnice("ugknbfddgicrmopn"), True)

    def test_isnice_case_3(self):
        self.assertEquals(day5.isnice("jchzalrnumimnmhp"), False)

    def test_isnice_case_4(self):
        self.assertEquals(day5.isnice("haegwjzuvuyypxyu"), False)

    def test_isnice_case_5(self):
        self.assertEquals(day5.isnice("dvszwmarrgswjxmb"), False)


class Criteria4Case(unittest.TestCase):
    def test_criteria4_case_1(self):
        self.assertEquals(day5.criteria4("xyxy"), True)

    def test_criteria4_case_2(self):
        self.assertEquals(day5.criteria4("aabcdefgaa"), True)

    def test_criteria4_case_3(self):
        self.assertEquals(day5.criteria4("aaa"), False)

    def test_criteria4_case_4(self):
        self.assertEquals(day5.criteria4("xxyxx"), True)


class Criteria5Case(unittest.TestCase):
    def test_criteria5_case_1(self):
        self.assertEquals(day5.criteria5("xyx"), True)

    def test_criteria5_case_2(self):
        self.assertEquals(day5.criteria5("abcdefeghi"), True)

    def test_criteria5_case_3(self):
        self.assertEquals(day5.criteria5("aaa"), True)

    def test_criteria5_case_4(self):
        self.assertEquals(day5.criteria5("xxyxx"), True)



class IsNicePart2Case(unittest.TestCase):
    def test_isnice_part2_case_1(self):
        self.assertEquals(day5.isnice("qjhvhtzxzqqjkmpb", "part2"), True)

    def test_isnice_part2_case_2(self):
        self.assertEquals(day5.isnice("xxyxx", "part2"), True)

    def test_isnice_part2_case_3(self):
        self.assertEquals(day5.isnice("uurcxstgmygtbstg", "part2"), False)

    def test_isnice_part2_case_4(self):
        self.assertEquals(day5.isnice("ieodomkazucvgmuy", "part2"), False)
