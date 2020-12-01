import unittest
import pytest
from .test_day import DayTest
from advent.advent2018 import day3


class GetClaimTestCase(unittest.TestCase):
    def test_get_claim(self):
        result = day3.get_claim("#123 @ 3,2: 5x4")
        self.assertIsInstance(result, day3.Claim)
        self.assertEqual(result.claim_id, 123)
        self.assertEqual(result.x, 3)
        self.assertEqual(result.y, 2)
        self.assertEqual(result.height, 5)
        self.assertEqual(result.width, 4)

    def test_get_bad_claim(self):
        with self.assertRaises(ValueError):
            day3.get_claim("")

        with self.assertRaises(ValueError):
            day3.get_claim("#123 @ 3,2: 5x4 3")


class SmallFabricTestCase(unittest.TestCase):
    def setUp(self):
        self.test_fabric = day3.Fabric(10)

    def test_empty_fabric(self):
        for i in range(10):
            for j in range(10):
                self.assertEqual(0, self.test_fabric.squares[i][j])

    def test_one_claim(self):
        self.test_fabric.add_claim(day3.Claim(123, 3, 2, 5, 4))
        self.assertEqual(self.test_fabric.squares[3][2], 1)

    def test_two_claims(self):
        self.test_fabric.add_claim(day3.Claim(123, 3, 2, 5, 4))
        self.test_fabric.add_claim(day3.Claim(124, 4, 5, 3, 3))
        self.assertEqual(self.test_fabric.get_num_squares_in_overlap(), 6)

    def test_three_claims(self):
        self.test_fabric.add_claim(day3.Claim(1, 1, 3, 4, 4))
        self.test_fabric.add_claim(day3.Claim(2, 3, 1, 4, 4))
        self.test_fabric.add_claim(day3.Claim(3, 5, 5, 2, 2))
        self.test_fabric.show()
        self.assertEqual(self.test_fabric.get_num_squares_in_overlap(), 4)


@pytest.mark.day
class TestDay3(DayTest):
    test_day = day3.Day3()
    expected_part_1 = ""
    expected_part_2 = ""
