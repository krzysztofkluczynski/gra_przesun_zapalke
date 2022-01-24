from colorama import Fore
from game.errors import (
    InvalidCharacterUsedError,
    InvalidEquationFormatError,
    EquationTooLongError,
    IndexValueError
)


def returnZero():
    return (
        " ______  \n"
        "|      | \n"
        "|      | \n"
        "|      | \n"
        "|      | \n"
        "|      | \n"
        "|______| \n"
    )


def returnOne():
    return (
        "         \n"
        "       | \n"
        "       | \n"
        "       | \n"
        "       | \n"
        "       | \n"
        "       | \n"
    )


def returnTwo():
    return (
        " ______  \n"
        "       | \n"
        "       | \n"
        " ______| \n"
        "|        \n"
        "|        \n"
        "|______  \n"
    )


def returnThree():
    return (
        " ______  \n"
        "       | \n"
        "       | \n"
        " ______| \n"
        "       | \n"
        "       | \n"
        " ______| \n"
    )


def returnFour():
    return (
        "         \n"
        "|      | \n"
        "|      | \n"
        "|______| \n"
        "       | \n"
        "       | \n"
        "       | \n"
    )


def returnFive():
    return (
        " ______  \n"
        "|        \n"
        "|        \n"
        "|______  \n"
        "       | \n"
        "       | \n"
        " ______| \n"
    )


def returnSix():
    return (
        " ______  \n"
        "|        \n"
        "|        \n"
        "|______  \n"
        "|      | \n"
        "|      | \n"
        "|______| \n"
    )


def returnSeven():
    return (
        " ______  \n"
        "|      | \n"
        "|      | \n"
        "|      | \n"
        "       | \n"
        "       | \n"
        "       | \n"
    )


def returnEight():
    return (
        " ______  \n"
        "|      | \n"
        "|      | \n"
        "|______| \n"
        "|      | \n"
        "|      | \n"
        "|______| \n"
    )


def returnNine():
    return (
        " ______  \n"
        "|      | \n"
        "|      | \n"
        "|______| \n"
        "       | \n"
        "       | \n"
        " ______| \n"
    )


def returnPlus():
    return (
        "         \n"
        "         \n"
        "         \n"
        "  __|__  \n"
        "    |    \n"
        "         \n"
        "         \n"
    )


def returnMinus():
    return (
        "        \n"
        "        \n"
        "        \n"
        "  ____  \n"
        "        \n"
        "        \n"
        "        \n"
    )


def returnEqual():
    return (
        "        \n"
        "        \n"
        "  ____  \n"
        "        \n"
        "  ____  \n"
        "        \n"
        "        \n"
    )


def returnMultiply():
    return (
        "        \n"
        "        \n"
        "        \n"
        "   \\/   \n"
        "   /\\   \n"
        "        \n"
        "        \n"
    )


def colored_plus(first_index, second_index, if_colored):
    """
    Returns ASCII ART plus,
    can be coloured
    """
    id_one = first_index
    id_two = second_index
    if if_colored:
        return (
            f"         \n"
            f"         \n"
            f"{Fore.BLUE}    {id_one}    {Fore.RESET}\n"
            f"{Fore.BLUE}  __|__{id_two} {Fore.RESET}\n"
            f"{Fore.BLUE}    |    {Fore.RESET}\n"
            f"         \n"
            f"         \n"
        )

    else:
        return (
            f"         \n"
            f"         \n"
            f"    {id_one}    \n"
            f"  {Fore.BLUE}__{Fore.RESET}|{Fore.BLUE}__{id_two}{Fore.RESET} \n"
            f"    |    \n"
            f"         \n"
            f"         \n"
        )


def vertical_up(index, if_colored: bool):
    """
    Returns vertical up match in each digit,
    It can be coloured
    """
    if if_colored:
        return (
            f" \n"
            f"{Fore.BLUE}|{Fore.RESET}\n"
            f"{Fore.BLUE}{index}{Fore.RESET}\n"
            f"{Fore.BLUE}|{Fore.RESET}\n"
        )
    else:
        return (
            f" \n"
            f"|\n"
            f"{index}\n"
            f"|\n"
        )


def vertical_down(index, if_colored: bool):
    """
    Returns vertical down match in each digit,
    It can be coloured
    """
    if if_colored:
        return (
            f"{Fore.BLUE}|{Fore.RESET}\n"
            f"{Fore.BLUE}{index}{Fore.RESET}\n"
            f"{Fore.BLUE}|{Fore.RESET}\n"
        )
    else:
        return (
            f"|\n"
            f"{index}\n"
            f"|\n"
        )


def horizontal(index, if_colored: bool):
    """
    Returns horizontal match in each digit,
    It can be coloured
    """
    if if_colored:
        if index in [3, 4, 5]:
            return (
                f"{Fore.BLUE}__{index}___{Fore.RESET}\n"
            )
        else:
            return (
                f"{Fore.BLUE}__{index}__{Fore.RESET}\n"
            )
    else:
        if index in [3, 4, 5]:
            return (
                f"__{index}___\n"
            )
        else:
            return (
                f"__{index}__\n"
            )


def left_side(index, if_first_colored: bool, if_second_colored: bool):
    """
    Creates left side of the digit using veritcal matches,
    It can be coloured
    """
    return (
        vertical_up(index, if_first_colored) +
        vertical_down(index+1, if_second_colored)
    )


def right_side(index, if_first_colored: bool, if_second_colored: bool):
    """
    Creates right side of the digit using veritcal matches,
    It can be coloured
    """
    whitespace_for_up_match = (
        " \n"
        " \n"
        " \n"
        " \n"
    )
    whitespace_for_down_match = (
        " \n"
        " \n"
        " \n"
    )

    up_part = vertical_up(index, if_first_colored)
    split_up_lines = zip(
        up_part.split('\n'),
        whitespace_for_up_match.split("\n")
        )
    result_up = '\n'.join([x + y for x, y in split_up_lines])

    down_part = vertical_down(index+1, if_second_colored)
    split_down_lines = zip(
        down_part.split('\n'),
        whitespace_for_down_match.split("\n")
        )
    result_down = '\n'.join([x + y for x, y in split_down_lines])

    return result_up + result_down


def mid(
    index,
    if_up_colored: bool,
    if_mid_colored: bool,
    if_down_colored: bool
):
    """
    Creates middle of the digit using horizontal matches,
    It can be coloured
    """
    if index == 3:
        whitespace = (
            "      \n"
            "      \n"
        )
        return (
            horizontal(index, if_up_colored) + whitespace +
            horizontal(index+1, if_mid_colored) + whitespace +
            horizontal(index+2, if_down_colored)
         )
    elif index == 10:
        whitespace = (
            "      \n"
            "     \n"
        )
        return (
            horizontal(index, if_up_colored) + whitespace +
            horizontal(index+1, if_mid_colored) + whitespace +
            horizontal(index+2, if_down_colored)
        )
    elif index >= 17:
        whitespace = (
            "      \n"
            "    \n"
        )
        return (
            horizontal(index, if_up_colored) + whitespace +
            horizontal(index+1, if_mid_colored) + whitespace +
            horizontal(index+2, if_down_colored)
        )
    else:
        raise IndexValueError(index)


def create_digit(index, number: str):
    """
    Creates coloured digit as an ASCII ART
    """
    dict_for_equation = {
        "0": [index, index+1, index+2, index+4, index+5, index+6],
        "1": [index+5, index+6],
        "2": [index+1, index+2, index+3, index+4, index+5],
        "3": [index+2, index+3, index+4, index+5, index+6],
        "4": [index, index+3, index+5, index+6],
        "5": [index, index+2, index+3, index+4, index+6],
        "6": [index, index+1, index+2, index+3, index+4, index+6],
        "7": [index, index+2, index+5, index+6],
        "8": [index, index+1, index+2, index+3, index+4, index+5, index+6],
        "9": [index, index+2, index+3, index+4, index+5, index+6],
    }
    colored_index_numbers = dict_for_equation[number]
    if index in colored_index_numbers:
        first_match = True
    else:
        first_match = False
    if index+1 in colored_index_numbers:
        second_match = True
    else:
        second_match = False
    if index+2 in colored_index_numbers:
        third_match = True
    else:
        third_match = False
    if index+3 in colored_index_numbers:
        fourth_match = True
    else:
        fourth_match = False
    if index+4 in colored_index_numbers:
        fifth_match = True
    else:
        fifth_match = False
    if index+5 in colored_index_numbers:
        sixth_match = True
    else:
        sixth_match = False
    if index+6 in colored_index_numbers:
        seventh_match = True
    else:
        seventh_match = False

    left = left_side(index, first_match, second_match)
    middle = mid(index+2, third_match, fourth_match, fifth_match)
    right = right_side(index+5, sixth_match, seventh_match)

    splt_lines = zip(left.split('\n'), middle.split("\n"), right.split("\n"))
    digit = '\n'.join([x + y + z for x, y, z in splt_lines])
    return digit


def create_description(equation):
    """
    Creates equation as an ASCII ART,
    every digit is '8' with coloured single matches
    """
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    first = 0
    second = 1
    index = 1
    listed_equation = list(equation)
    if listed_equation[0].isdigit():
        result = create_digit(index, listed_equation[0])
        index += 7
    elif listed_equation[0] == "+":
        result = colored_plus(alphabet[first], alphabet[second], True)
        first += 2
        second += 2
    elif listed_equation[0] == "-":
        result = colored_plus(alphabet[first], alphabet[second], False)
        first += 2
        second += 2
    for element in listed_equation[1:]:
        if element.isdigit():
            number = create_digit(index, element)
            splt_lines = zip(result.split('\n'), number.split("\n"))
            result = '\n'.join([x + y for x, y in splt_lines])
            index += 7
        else:
            if element == "+":
                sign = colored_plus(alphabet[first], alphabet[second], True)
                splt_lines = zip(result.split('\n'), sign.split("\n"))
                result = '\n'.join([x + y for x, y in splt_lines])
                first += 2
                second += 2
            elif element == "-":
                sign = colored_plus(alphabet[first], alphabet[second], False)
                splt_lines = zip(result.split('\n'), sign.split("\n"))
                result = '\n'.join([x + y for x, y in splt_lines])
                first += 2
                second += 2
            elif element == "=":
                sign = returnEqual()
                splt_lines = zip(result.split('\n'), sign.split("\n"))
                result = '\n'.join([x + y for x, y in splt_lines])
            elif element == "*":
                sign = returnMultiply()
                splt_lines = zip(result.split('\n'), sign.split("\n"))
                result = '\n'.join([x + y for x, y in splt_lines])

    return result


def create_equation(equation):
    """
    Creates equation as an ASCII ART,
    every symbol has it own representation
    """
    dict_for_equation = {
        "0": returnZero(),
        "1": returnOne(),
        "2": returnTwo(),
        "3": returnThree(),
        "4": returnFour(),
        "5": returnFive(),
        "6": returnSix(),
        "7": returnSeven(),
        "8": returnEight(),
        "9": returnNine(),
        "-": returnMinus(),
        "+": returnPlus(),
        "=": returnEqual(),
        "*": returnMultiply()
    }
    check_equation(equation)
    listed_equation = list(equation)
    multiline_equation = dict_for_equation[listed_equation[0]]
    for element in listed_equation[1:]:
        number = dict_for_equation[element]
        splt_lines = zip(multiline_equation.split('\n'), number.split("\n"))
        multiline_equation = '\n'.join([x + y for x, y in splt_lines])
    return multiline_equation


def check_equation(equation):
    """
    Check if the equation is valid and if the programme is able to create it
    """
    characters = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "+",
        "-",
        "=",
        "*"
        ]
    listed_equation = list(equation)
    for element in listed_equation:
        if element not in characters:
            raise InvalidCharacterUsedError(equation)
    if len(listed_equation) > 10:
        raise EquationTooLongError(equation)
    if (
        listed_equation.count("=") > 1 or
        listed_equation.count("+") > 2 or
        listed_equation.count("-") > 2
    ):
        raise InvalidEquationFormatError(equation)
    if listed_equation[-1] in ["+", "-", "=", "*"]:
        raise InvalidEquationFormatError(equation)
    if listed_equation[0] in ["*", "="]:
        raise InvalidEquationFormatError(equation)
    for i, element in enumerate(listed_equation):
        if element in ["+", "-", "*"]:
            if listed_equation[i] == listed_equation[i+1]:
                raise InvalidEquationFormatError(equation)
