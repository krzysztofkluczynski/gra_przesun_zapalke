import json
from game.levels_classes import (
    EasyAndMediumLevel,
    HardLevel,
)
from game.errors import (
    JsonDataErrorInEasy,
    JsonDataErrorInMedium,
    JsonDataErrorInHard,
    JsonDataErrorInUser
)


def read_easy_levels_from_json(handle):
    """
    Function reads easy levels from json file,
    returns a list of levels
    """
    try:
        data = json.load(handle)
        easy_levels = []
        for level in data["built_in_levels"]["easy"]:
            task = level["task"]
            equation = level["equation"]
            first_move = level["first_move"]
            second_move = level["second_move"]
            created_easy_level = EasyAndMediumLevel(
                equation,
                task,
                first_move,
                second_move)
            easy_levels.append(created_easy_level)
    except Exception:
        raise JsonDataErrorInEasy
    return easy_levels


def read_medium_levels_from_jason(handle):
    """
    Function reads medium levels from json file,
    returns a list of levels
    """
    try:
        data = json.load(handle)
        medium_levels = []
        for level in data["built_in_levels"]["medium"]:
            task = level["task"]
            equation = level["equation"]
            first_move = level["first_move"]
            second_move = level["second_move"]
            created_medium_level = EasyAndMediumLevel(
                equation,
                task,
                first_move,
                second_move)
            medium_levels.append(created_medium_level)
    except Exception:
        raise JsonDataErrorInMedium
    return medium_levels


def read_hard_levels_from_jason(handle):
    """
    Function reads hard levels from json file,
    returns a list of levels
    """
    try:
        data = json.load(handle)
        hard_levels = []
        for level in data["built_in_levels"]["hard"]:
            task = level["task"]
            equation = level["equation"]
            first_move = level["first_move"]
            second_move = level["second_move"]
            created_hard_level = HardLevel(
                equation,
                task,
                first_move,
                second_move
                )
            hard_levels.append(created_hard_level)
    except Exception:
        raise JsonDataErrorInHard
    return hard_levels


def read_user_levels_from_jason(handle):
    """
    Function reads user levels from json file,
    returns a list of levels
    """
    try:
        data = json.load(handle)
        user_levels = []
        for level in data["created_by_user"]:
            task = level["task"]
            equation = level["equation"]
            first_move = level["first_move"]
            second_move = level["second_move"]
            created_user_level = EasyAndMediumLevel(
                equation,
                task,
                first_move,
                second_move
                )
            user_levels.append(created_user_level)
    except Exception as e:
        print(e)
        raise JsonDataErrorInUser
    return user_levels
