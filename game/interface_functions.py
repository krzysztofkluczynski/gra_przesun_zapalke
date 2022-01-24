from game.errors import (
    InvalidInputError,
    InputOutOfRange,
    InvalidCharacterUsedError
)
from random import choice

from game.making_ascii_equation import (
    create_description,
    create_equation
)


def get_user_input():
    """
    Function manges menu input from user
    """
    data = (input("Your choice: "))
    if data not in ["1", "2", "3", "4"]:
        raise InvalidInputError(data)
    return data


def choose_difficulty():
    '''
    Function returns some menu options to choose from
    '''
    return (
        "Choose difficulty:\n"
        "1) Easy\n"
        "2) Medium\n"
        "3) Hard\n"
        "4) Quit\n"
        )


def roll_random_level(levels):
    '''
    Function rolls random level from given list.
    Used in each level play
    '''
    level = choice(levels)
    return level


def yes_or_no_answer(input):
    '''
    Function manages the frequently occuring yes/no questions
    '''
    if input in ["y", "Y", "Yes", "yes", "YES"]:
        return True
    elif input in ["n", "no", "N", "No", "NO"]:
        return False
    else:
        raise InvalidInputError(input)


def calculate_last_index(equation):
    '''
    Function calculates index of last digit in the equation
    '''
    index = 0
    listed_equation = list(equation)
    for element in listed_equation:
        if element.isdigit():
            index += 7
    return index


def calculate_last_letter(equation):
    '''
    Function calculates number of the last occuring letter in equation
    '''
    number = 0
    listed_equation = list(equation)
    for element in listed_equation:
        if element in ["+", "-"]:
            number += 2
    return number


def user_creates_his_equation(equation):
    '''
    Function lets user make his own level using other functions.
    Also checks if user level make sense
    '''
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n"]
    available_letters = letters[:calculate_last_letter(equation)]
    print(create_equation(equation))
    print("There are numbers of matches: ")
    print(create_description(equation))
    answers = get_level_input(1)
    index = calculate_last_index(equation)
    if answers[0] == answers[1]:
        raise InvalidCharacterUsedError(answers)
    if answers[0].isdigit():
        if (
            int(answers[0]) > index or
            int(answers[0]) < 1 or
            int(answers[1]) > index or
            int(answers[1]) < 1
        ):
            raise InputOutOfRange(index)
    else:
        if answers[0] not in available_letters:
            raise InvalidCharacterUsedError(answers[0])
    if answers[1].isdigit():
        if int(answers[1]) > index or int(answers[1]) < 1:
            raise InputOutOfRange(answers[1])
    else:
        if answers[1] not in available_letters:
            raise InvalidCharacterUsedError(answers[1])
    return answers[0], answers[1]


def play_one_level(current_level):
    ''''
    Function lets user to play a single level
    '''
    print(str(current_level))
    answers = get_level_input(current_level.get_matches_to_move())
    if len(answers) == 2:
        if_correct = current_level.check_if_correct(answers[0], answers[1])
    elif len(answers) == 4:
        if_correct = current_level.check_if_correct(
            answers[0],
            answers[1],
            answers[2],
            answers[3]
            )
    if if_correct:
        return True
    else:
        return False


def get_level_input(matches_to_move):
    '''
    Function asks user for input depending on number of matches to move
    '''
    user_answers = []
    for moves in range(0, matches_to_move):
        choosen_match = input("Choose a match you want to move: ")
        place_for_match = input("Choose a place for your match: ")
        user_answers.append(choosen_match)
        user_answers.append(place_for_match)
    return user_answers
