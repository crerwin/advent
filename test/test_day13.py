import unittest
from days import day13


class ParseTest(unittest.TestCase):
    def test_parse_1(self):
        self.assertEqual(day13.parser("Alice would gain 54 happiness units by sitting next to Bob."), ("Alice", "Bob", 54))

    def test_parse_2(self):
        self.assertEqual(day13.parser("Alice would lose 79 happiness units by sitting next to Carol."), ("Alice", "Carol", -79))
