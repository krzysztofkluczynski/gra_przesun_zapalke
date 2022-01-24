from game.levels_classes import (
    Level,
    EasyAndMediumLevel,
    HardLevel
)


def test_create_level():
    level = Level(
        "3+12=15",
        "Move one match to make the equation correct",
        "1",
        "23"
    )
    assert level.get_equation() == "3+12=15"
    assert level.get_task() == "Move one match to make the equation correct"
    assert level.get_first_answer() == "1"
    assert level.get_second_answer() == "23"
    assert level.get_last_index() == 35
    assert level.get_matches_to_move() == 0


def test_check_correct_answers_easy():
    level_easy = EasyAndMediumLevel(
        "31-2=29",
        "move one match",
        "1",
        "2",
    )
    assert level_easy.check_if_correct("1", "2") is True


def test_check_wrong_answers_easy():
    level_easy = EasyAndMediumLevel(
        "31-2=29",
        "move one match",
        "1",
        "2",
    )
    assert level_easy.check_if_correct("3", "4") is False
    assert level_easy.check_if_correct("2", "1") is False


def test_check_correct_answers_hard():
    level_easy = HardLevel(
        "31-2=29",
        "move two matches match",
        ["1", "2"],
        ["3", "4"],
    )
    assert level_easy.check_if_correct("1", "3", "2", "4") is True
    assert level_easy.check_if_correct("2", "4", "1", "3") is True
    assert level_easy.check_if_correct("2", "3", "1", "4") is True
    assert level_easy.check_if_correct("1", "4", "2", "3") is True


def test_check_wrong_answers_hard():
    level_easy = HardLevel(
        "31-2=29",
        "move two matches match",
        ["1", "2"],
        ["3", "4"],
    )
    assert level_easy.check_if_correct("1", "1", "2", "4") is False
    assert level_easy.check_if_correct("1", "2", "1", "4") is False
    assert level_easy.check_if_correct("1", "2", "3", "4") is False
    assert level_easy.check_if_correct("1", "4", "2", "4") is False
