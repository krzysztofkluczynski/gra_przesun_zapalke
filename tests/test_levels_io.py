from io import StringIO
import pytest
from game.errors import (
    JsonDataErrorInEasy,
    JsonDataErrorInMedium,
    JsonDataErrorInHard,
    JsonDataErrorInUser
)
from game.levels_io import (
    read_easy_levels_from_json,
    read_medium_levels_from_jason,
    read_hard_levels_from_jason,
    read_user_levels_from_jason
)

levels_string = '''
{
"built_in_levels": {
    "easy": [
    {
        "equation": "2",
        "task": "Move one match to make number three:",
        "first_move": "2",
        "second_move": "7"
    },
    {
        "equation": "6",
        "task": "Move one match to make number nine:",
        "first_move": "2",
        "second_move": "6"
    },
    {
        "equation": "3",
        "task": "Move one match to make number five:",
        "first_move": "6",
        "second_move": "1"
    }
    ],
    "medium": [
    {
        "equation": "23+8=25",
        "task": "move one match to make the equation correct:",
        "first_move": "20",
        "second_move": "34"
    },
    {
        "equation": "9-5=9",
        "task": "move one match to make the equation correct:",
        "first_move": "15",
        "second_move": "9"
    },
    {
        "equation": "12+11=22",
        "task": "move one match to make the equation correct:",
        "first_move": "37",
        "second_move": "42"
    },
    {
        "equation": "1+2-3=1",
        "task": "move one match to make the equation correct:",
        "first_move": "21",
        "second_move": "16"
    }
    ],
    "hard": [
    {
        "equation": "9+6=16",
        "task": "move two matches to make the equation correct:",
        "first_move": [
        "9",
        "23"
        ],
        "second_move": [
        "2",
        "27"
        ]
    },
    {
        "equation": "4*9=46",
        "task": "move two matches to make the equation correct:",
        "first_move": [
        "13",
        "23"
        ],
        "second_move": [
        "3",
        "5"
        ]
    }
    ]
}
}
'''


def test_read_easy_levels_from_json_correct():
    levels = read_easy_levels_from_json(StringIO(levels_string))
    assert len(levels) == 3
    assert levels[1].get_equation() == "6"
    assert levels[1].get_task() == "Move one match to make number nine:"
    assert levels[1].get_first_answer() == "2"
    assert levels[1].get_second_answer() == "6"
    assert levels[2].get_equation() == "3"
    assert levels[2].get_task() == "Move one match to make number five:"


def test_read_medium_levels_from_json_correct():
    levels = read_medium_levels_from_jason(StringIO(levels_string))
    assert len(levels) == 4
    assert levels[1].get_equation() == "9-5=9"
    assert levels[1].get_task() == (
        "move one match to make the equation correct:"
    )
    assert levels[3].get_equation() == "1+2-3=1"
    assert levels[3].get_task() == (
        "move one match to make the equation correct:"
    )


def test_read_hard_levels_from_json_correct():
    levels = read_hard_levels_from_jason(StringIO(levels_string))
    assert len(levels) == 2
    assert levels[0].get_equation() == "9+6=16"
    assert levels[0].get_task() == (
        "move two matches to make the equation correct:"
    )
    assert levels[0].get_first_answer() == ["9", "23"]
    assert levels[1].get_equation() == "4*9=46"
    assert levels[1].get_task() == (
        "move two matches to make the equation correct:"
    )
    assert levels[1].get_second_answer() == ["3", "5"]


def test_read_user_levels_from_json_empty():
    data = '''
    {
    "created_by_user": []
    }
    '''
    levels = read_user_levels_from_jason(StringIO(data))
    assert len(levels) == 0


def test_read_user_levels_from_json_correct():
    data = '''
    {
    "created_by_user": [
        {
            "equation": "3",
            "task": "move one match:",
            "first_move": "1",
            "second_move": "2"
        }
    ]
    }
    '''
    levels = read_user_levels_from_jason(StringIO(data))
    assert len(levels) == 1
    assert levels[0].get_equation() == "3"


def test_read_user_levels_from_json_correct_few_levels():
    data = '''
    {
    "created_by_user": [
        {
        "equation": "2+2=4",
        "task": "Move one match to make the equation correct",
        "first_move": "a",
        "second_move": "b"
        },
        {
        "equation": "1+4=5",
        "task": "Move one match to make the equation correct",
        "first_move": "a",
        "second_move": "3"
        }
    ]
    }
    '''
    levels = read_user_levels_from_jason(StringIO(data))
    assert len(levels) == 2
    assert levels[1].get_first_answer() == "a"
    assert levels[0].get_task() == (
        "Move one match to make the equation correct"
    )


def test_mal_formed_easy_levels_key_value_error():
    data_string = '''
    {
        "built_in_levels": {
        "easy": [
            {
            "eq": "2",
            "task": "Move one match to make number three:",
            "first_move": "2",
            "second_move": "7"
            },
            {
            "equation": "6",
            "task": "Move one match to make number nine:",
            "first_move": "2",
            "second_move": "6"
            },
            {
            "equation": "3",
            "task": "Move one match to make number five:",
            "first_move": "6",
            "second_move": "1"
            }
        ]
        }
    }
    '''
    with pytest.raises(JsonDataErrorInEasy):
        read_easy_levels_from_json(StringIO(data_string))


def test_mal_formed_medium_levels_wrong_formed_json_comma():
    data_string = '''
    {
        "built_in_levels": {
        "medium": [
            {
            "equation": "2"
            "task": "Move one match to make number three:",
            "first_move": "2",
            "second_move": "7"
            },
            {
            "equation": "6",
            "task": "Move one match to make number nine:",
            "first_move": "2",
            "second_move": "6"
            },
            {
            "equation": "3",
            "task": "Move one match to make number five:",
            "first_move": "6",
            "second_move": "1"
            }
        ]
        }
    }
    '''
    with pytest.raises(JsonDataErrorInMedium):
        read_medium_levels_from_jason(StringIO(data_string))


def test_mal_formed_hard_levels_missing_key():
    data_string = '''
    {
        "built_in_levels": {
        "hard": [
            {
            "equation": "2"
            "task": "Move one match to make number three:",
            "first_move": "2",
            },
            {
            "equation": "6",
            "task": "Move one match to make number nine:",
            "first_move": "2",
            "second_move": "6"
            },
            {
            "equation": "3",
            "task": "Move one match to make number five:",
            "first_move": "6",
            "second_move": "1"
            }
        ]
        }
    }
    '''
    with pytest.raises(JsonDataErrorInHard):
        read_hard_levels_from_jason(StringIO(data_string))


def test_key_error_user_levels_json():
    data_string = '''
    {
    "user": [
        {
            "equation": "3",
            "task": "move one match:",
            "first_move": "1",
            "second_move": "2"
        }
    ]
    }
    '''
    with pytest.raises(JsonDataErrorInUser):
        read_user_levels_from_jason(StringIO(data_string))


def test_empty_list_user_levels_json():
    data_string = '''
    {
    "created_by_user": []
    }
    '''
    assert read_user_levels_from_jason(StringIO(data_string)) == []


def test_empty_user_levels_json_file():
    data_string = '''

    '''
    with pytest.raises(JsonDataErrorInUser):
        read_user_levels_from_jason(StringIO(data_string))
