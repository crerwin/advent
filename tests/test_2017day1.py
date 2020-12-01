import pytest
from .test_day import DayTest
from advent.advent2017 import day1


def test_captcha():
    assert day1.process_captcha("") == 0
    assert day1.process_captcha("1122") == 3
    assert day1.process_captcha("1111") == 4
    assert day1.process_captcha("1234") == 0
    assert day1.process_captcha("91212129") == 9


def test_captcha2():
    assert day1.process_captcha_2("") == 0
    assert day1.process_captcha_2("1212") == 6
    assert day1.process_captcha_2("1221") == 0
    assert day1.process_captcha_2("123425") == 4
    assert day1.process_captcha_2("123123") == 12
    assert day1.process_captcha_2("12131415") == 4


@pytest.mark.day
class TestDay1(DayTest):
    test_day = day1.Day1()
    expected_part_1 = "1141"
    expected_part_2 = "950"
