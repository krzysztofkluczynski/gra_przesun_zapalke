from io import StringIO
from game.interface_functions import (
    calculate_last_letter,
    get_user_input,
    yes_or_no_answer,
    calculate_last_index
)
from game.errors import (
    InvalidInputError,
)
import pytest


def test_get_user_input_correct_int(monkeypatch):
    number_inputs = StringIO("1")
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert get_user_input() == "1"


def test_get_user_input_out_of_range(monkeypatch):
    number_inputs = StringIO("5")
    monkeypatch.setattr('sys.stdin', number_inputs)
    with pytest.raises(InvalidInputError):
        get_user_input()


def test_get_user_input_invalid_character(monkeypatch):
    number_inputs = StringIO("A")
    monkeypatch.setattr('sys.stdin', number_inputs)
    with pytest.raises(InvalidInputError):
        get_user_input()


def test_yes_or_no_answer_true():
    assert yes_or_no_answer("y") is True
    assert yes_or_no_answer("yes") is True
    assert yes_or_no_answer("YES") is True
    assert yes_or_no_answer("Y") is True


def test_yes_or_no_answer_false():
    assert yes_or_no_answer("n") is False
    assert yes_or_no_answer("No") is False
    assert yes_or_no_answer("NO") is False
    assert yes_or_no_answer("N") is False


def test_yes_or_no_answer_invalid():
    with pytest.raises(InvalidInputError):
        yes_or_no_answer("abcd")


def test_calculate_last_index_correct():
    assert calculate_last_index("3") == 7
    assert calculate_last_index("33") == 14
    assert calculate_last_index("1+2+3=234") == 42


def test_calculate_last_letter_number():
    assert calculate_last_letter("132123") == 0
    assert calculate_last_letter("123") == 0
    assert calculate_last_letter("1+2+3=6") == 4
    assert calculate_last_letter("1+2-3*8=-21") == 6
