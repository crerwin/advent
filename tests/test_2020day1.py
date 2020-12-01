import unittest
import pytest
from .test_day import DayTest
from advent.advent2020 import day1


class GetProdTestCase(unittest.TestCase):
    def test_get_prod(self):
        inputs = ["1721", "979", "366", "299", "675", "1456"]
        self.assertEqual(day1.get_prod(inputs), 514579)


@pytest.mark.day
class TestDay1(DayTest):
    test_day = day1.Day1()
    expected_part_1 = "145875"
    expected_part_2 = "69596112"
