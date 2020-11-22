import unittest
from tests.test_day import DayTest
from advent.advent2015 import day4


class HashCase(unittest.TestCase):
    def test_hash_case_1(self):
        hash = day4.hashvalue("abcdef", "609043")
        self.assertEqual(hash[:11], "000001dbbfa")

    def test_hash_case_2(self):
        hash = day4.hashvalue("pqrstuv", "1048970")
        self.assertEqual(hash[:11], "000006136ef")


class IsValidHashCase(unittest.TestCase):
    def test_validhash_case_1(self):
        self.assertEqual(day4.isvalidhash("000001dbbfa"), True)

    def test_validhash_case_2(self):
        self.assertEqual(day4.isvalidhash("your mom"), False)

    def test_validhash_case_3(self):
        self.assertEqual(day4.isvalidhash(""), False)


class FindValidHashCase(unittest.TestCase):
    def test_findhash_case_1(self):
        self.assertEqual(day4.findvalidhash("abcdef"), "609043")

    def test_findhash_case_1(self):
        self.assertEqual(day4.findvalidhash("pqrstuv"), "1048970")


class Day4Test(DayTest):
    test_day = day4.Day4()
    expected_part_1 = "117946"
    expected_part_2 = "3938038"