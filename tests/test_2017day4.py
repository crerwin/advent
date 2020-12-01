import pytest
from .test_day import DayTest
from advent.advent2017 import day4


def test_is_valid_passphrase():
    assert not day4.is_valid_passphrase("hello")
    assert not day4.is_valid_passphrase("aa bb cc dd aa")
    assert day4.is_valid_passphrase("aa bb cc dd ee")
    assert day4.is_valid_passphrase("aa bb cc dd aaa")


def test_is_anagram():
    assert day4.is_anagram("hello", "loleh")
    assert not day4.is_anagram("hello", "lolah")
    assert not day4.is_anagram("a", "ab")
    assert not day4.is_anagram("ab", "abc")
    assert not day4.is_anagram("abc", "abd")


def test_is_valid_passphrase_2():
    assert day4.is_valid_passphrase_2("abcde fghij")
    assert not day4.is_valid_passphrase_2("abcde xyz ecdab")
    assert day4.is_valid_passphrase_2("a ab abc abd abf abj")
    assert day4.is_valid_passphrase_2("iiii oiii ooii oooi oooo")
    assert not day4.is_valid_passphrase_2("oiii ioii iioi iiio")


@pytest.mark.day
class TestDay4(DayTest):
    test_day = day4.Day4()
    expected_part_1 = "386"
    expected_part_2 = "208"
