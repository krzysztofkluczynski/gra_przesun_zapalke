from game.making_ascii_equation import (
    create_equation,
    create_description
)
from game.interface_functions import calculate_last_index


class Level():
    """
    Class of each level
    """
    def __init__(self, equation, task, first_answer, second_answer):
        self._last_index = calculate_last_index(equation)
        self._equation = equation
        self._task = task
        self._first_answer = first_answer
        self._second_answer = second_answer
        self._matches_to_move = 0

    def get_equation(self):
        return self._equation

    def get_task(self):
        return self._task

    def get_first_answer(self):
        return self._first_answer

    def get_second_answer(self):
        return self._second_answer

    def get_last_index(self):
        return self._last_index

    def get_matches_to_move(self):
        return self._matches_to_move

    def __str__(self):
        """
        Represents level as a string
        """
        result = (
            self._task +
            "\n" +
            create_equation(self._equation) +
            "\n"
            "There are numbers assimilated to each match: \n" +
            "\n" +
            create_description(self._equation)
        )
        return result


class EasyAndMediumLevel(Level):
    """
    Class of easy and medium levels,
    User has to move one match in this type of levels
    """
    def __init__(self, equation, task, first_move, second_move):
        super().__init__(equation, task, first_move, second_move)
        self._matches_to_move = 1

    def check_if_correct(self, first_user_move, second_user_move):
        """
        Check if given arguments match the level answers
        """
        if (
            self._first_answer == first_user_move and
            self._second_answer == second_user_move
        ):
            return True
        else:
            return False


class HardLevel(Level):
    """
    Class of easy and medium levels,
    User has to move two matches in this type of levels
    """
    def __init__(self, equation, task, first_answer, second_answer):
        super().__init__(equation, task, first_answer, second_answer)
        self._matches_to_move = 2

    def check_if_correct(
        self,
        first_user_move,
        second_user_move,
        third_user_move,
        fourth_user_move
    ):
        """
        Check if given arguments match the level answers
        """
        if (
            first_user_move == self._first_answer[0] and
            second_user_move == self._second_answer[0]
        ):
            if (
                third_user_move == self._first_answer[1] and
                fourth_user_move == self._second_answer[1]
            ):
                return True
            else:
                return False
        elif (
            first_user_move == self._first_answer[0] and
            second_user_move == self._second_answer[1]
        ):
            if (
                third_user_move == self._first_answer[1] and
                fourth_user_move == self._second_answer[0]
            ):
                return True
            else:
                return False
        elif (
            first_user_move == self._first_answer[1] and
            second_user_move == self._second_answer[0]
        ):
            if (
                third_user_move == self._first_answer[0] and
                fourth_user_move == self._second_answer[1]
            ):
                return True
            else:
                return False
        elif (
            first_user_move == self._first_answer[1] and
            second_user_move == self._second_answer[1]
        ):
            if (
                third_user_move == self._first_answer[0] and
                fourth_user_move == self._second_answer[0]
            ):
                return True
            else:
                return False
        else:
            return False
