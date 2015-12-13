import unittest
import day6


class InitTest(unittest.TestCase):
    def test1(self):
        day6.init()


class ParseLineTestCase(unittest.TestCase):
    def test1(self):
        day6.parseline("turn off 660,55 through 986,197")