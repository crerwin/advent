import unittest
from advent.advent2015 import day10


class LookAndSayTestCase(unittest.TestCase):
    def test1(self):
        result = day10.lookAndSay("1")
        self.assertEqual("11", result)

    def test2(self):
        result = day10.lookAndSay("11")
        self.assertEqual("21", result)

    def test3(self):
        result = day10.lookAndSay("21")
        self.assertEqual("1211", result)

    def test4(self):
        result = day10.lookAndSay("1211")
        self.assertEqual("111221", result)

    def test5(self):
        result = day10.lookAndSay("111221")
        self.assertEqual("312211", result)

    def test_iteration(self):
        result = day10.iterate("1", 5)
        self.assertEqual("312211", result)
