import unittest
import pytest
from .test_day import DayTest
from advent.advent2022 import day2


class TestScoreRound(unittest.TestCase):
    def setUp(self) -> None:
        self.test_inputs = [
            "A Y",
            "B X",
            "C Z",
        ]

    def test_score_round_raises(self):
        with self.assertRaises(ValueError):
            day2.score_round("fd")

        with self.assertRaises(ValueError):
            day2.score_round("A")

        with self.assertRaises(ValueError):
            day2.score_round("A ")

        with self.assertRaises(ValueError):
            day2.score_round("A Y ")

        with self.assertRaises(ValueError):
            day2.score_round("D Y")

        with self.assertRaises(ValueError):
            day2.score_round("A W")

    def test_score_round(self):
        self.assertEqual(day2.score_round("A Y"), 8)
        self.assertEqual(day2.score_round("B X"), 1)
        self.assertEqual(day2.score_round("C Z"), 6)

    def test_score_game(self):
        self.assertEqual(day2.score_game(self.test_inputs), 15)


class TestOutcomeScore(unittest.TestCase):
    def test_outcome_score(self):
        # wins
        self.assertEqual(day2.outcome_score("A", "B"), 6)
        self.assertEqual(day2.outcome_score("B", "C"), 6)
        self.assertEqual(day2.outcome_score("C", "A"), 6)

        # losses
        self.assertEqual(day2.outcome_score("B", "A"), 0)
        self.assertEqual(day2.outcome_score("C", "B"), 0)
        self.assertEqual(day2.outcome_score("A", "C"), 0)

        # draws
        self.assertEqual(day2.outcome_score("A", "A"), 3)
        self.assertEqual(day2.outcome_score("B", "B"), 3)
        self.assertEqual(day2.outcome_score("C", "C"), 3)


@pytest.mark.day
class TestDay2(DayTest):
    test_day = day2.Day2()
    expected_part_1 = "11386"
    expected_part_2 = "13600"
