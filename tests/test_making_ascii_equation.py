from game.making_ascii_equation import (
    create_equation,
    create_digit,
    horizontal,
    left_side,
    mid,
    right_side,
    vertical_down,
    vertical_up,
)
from game.errors import (
    IndexValueError,
    InvalidCharacterUsedError,
    EquationTooLongError,
    InvalidEquationFormatError
)
import pytest


def test_create_equation_invalid_character():
    with pytest.raises(InvalidCharacterUsedError):
        create_equation("a")


def test_create_equation_too_long():
    with pytest.raises(EquationTooLongError):
        create_equation("1234+1234=10")


def test_create_equation_wrong_first_sign():
    with pytest.raises(InvalidEquationFormatError):
        create_equation("=123")


def test_create_equation_more_than_3_plus():
    with pytest.raises(InvalidEquationFormatError):
        create_equation("+17+2+3=1")


def test_create_description_space_bars():
    with pytest.raises(InvalidCharacterUsedError):
        create_equation("2 + 2")


def test_create_equation_two_same_signs():
    with pytest.raises(InvalidEquationFormatError):
        create_equation("3++3")


def test_create_description_invalid_ending_():
    with pytest.raises(InvalidEquationFormatError):
        create_equation("2+")


def test_create_description_invalid_ending_minus():
    with pytest.raises(InvalidEquationFormatError):
        create_equation("2+2-3-")


def test_create_description_invalid_ending_multiply():
    with pytest.raises(InvalidEquationFormatError):
        create_equation("2231*")


def test_create_digit_invalid_index():
    with pytest.raises(IndexValueError):
        create_digit(2, "3")


def test_create_equation_single_digit():
    assert create_equation("8") == (
        " ______  \n"
        "|      | \n"
        "|      | \n"
        "|______| \n"
        "|      | \n"
        "|      | \n"
        "|______| \n"
    )


def test_create_equation_two_digits():
    assert create_equation("63") == (
        " ______   ______  \n"
        "|               | \n"
        "|               | \n"
        "|______   ______| \n"
        "|      |        | \n"
        "|      |        | \n"
        "|______|  ______| \n"
    )


def test_create_equation_real_equation():
    assert create_equation("6+3=9") == (
        " ______            ______           ______  \n"
        "|                        |         |      | \n"
        "|                        |   ____  |      | \n"
        "|______    __|__   ______|         |______| \n"
        "|      |     |           |   ____         | \n"
        "|      |                 |                | \n"
        "|______|           ______|          ______| \n"
    )


def test_create_equation_real_equation_multiply():
    assert create_equation("2*3=6") == (
        " ______           ______           ______  \n"
        "       |                |         |        \n"
        "       |                |   ____  |        \n"
        " ______|    \\/    ______|         |______  \n"
        "|           /\\          |   ____  |      | \n"
        "|                       |         |      | \n"
        "|______           ______|         |______| \n"
    )


def test_vertical_down():
    assert vertical_down(1, False) == (
        "|\n"
        "1\n"
        "|\n"
    )


def test_vertical_up():
    assert vertical_up(22, False) == (
        " \n"
        "|\n"
        "22\n"
        "|\n"
    )


def test_horizontal():
    assert horizontal(3, False) == (
        "__3___\n"
    )


def test_horizontal_bigger_index():
    assert horizontal(13, False) == (
        "__13__\n"
    )


def test_left_side_first():
    assert left_side(1, False, False) == (
        " \n"
        "|\n"
        "1\n"
        "|\n"
        "|\n"
        "2\n"
        "|\n"
    )


def test_left_side_second():
    assert left_side(8, False, False) == (
        " \n"
        "|\n"
        "8\n"
        "|\n"
        "|\n"
        "9\n"
        "|\n"
    )


def test_left_side_third():
    assert left_side(16, False, False) == (
        " \n"
        "|\n"
        "16\n"
        "|\n"
        "|\n"
        "17\n"
        "|\n"
    )


def test_mid_invalod_index():
    with pytest.raises(IndexValueError):
        mid(1, False, False, False)


def test_mid_correct_index_single_digit():
    assert mid(3, False, False, False) == (
        "__3___\n"
        "      \n"
        "      \n"
        "__4___\n"
        "      \n"
        "      \n"
        "__5___\n"
    )


def test_mid_correct_index_two_digit_number():
    assert mid(10, False, False, False) == (
        "__10__\n"
        "      \n"
        "     \n"
        "__11__\n"
        "      \n"
        "     \n"
        "__12__\n"
    )


def test_mid_correct_index_two_digit_number_biggr_tahn_17():
    assert mid(24, False, False, False) == (
        "__24__\n"
        "      \n"
        "    \n"
        "__25__\n"
        "      \n"
        "    \n"
        "__26__\n"
    )


def test_right_side():
    assert right_side(6, False, False) == (
        "  \n"
        "| \n"
        "6 \n"
        "| \n"
        "| \n"
        "7 \n"
        "| \n"
    )


def test_right_side_two_digit_number():
    assert right_side(55, False, False) == (
        "  \n"
        "| \n"
        "55 \n"
        "| \n"
        "| \n"
        "56 \n"
        "| \n"
    )
