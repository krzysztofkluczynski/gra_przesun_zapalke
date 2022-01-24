from game.levels_io import read_user_levels_from_jason
from game.interface_functions import (
    get_user_input,
    choose_difficulty,
    roll_random_level,
    yes_or_no_answer,
    user_creates_his_equation,
    play_one_level,
)

from game.errors import (
    InvalidInputError,
)

from game.making_ascii_equation import (
    check_equation,
)
import json
import copy

options = (
    "MENU:\n"
    "1. Play default levels\n"
    "2. Play levels created by the user\n"
    "3. Add level\n"
    "4. Quit\n"
    )

instructions = (
    "You are creating your own level now.\n"
    "There are some rules you need to follow:\n"
    "\n"
    "1. You can only use digits and signs: +, -, * and =.\n"
    "2. You cannot use space bars.\n"
    "3. You cannot use more than 10 characters.\n"
    "4. You can use just one =. \n"
    "5. You can use only less than 3 +/- signs.\n"
    "6. The equation cannot start with =/*. \n"
        )


class Interface():
    """
    Class of interface
    """
    def __init__(
        self,
        user_level_path: str,
        easy_levels,
        medium_levels,
        hard_levels
    ):
        self._user_level_path = user_level_path
        self._easy_levels = easy_levels
        self._medium_levels = medium_levels
        self._hard_levels = hard_levels

    def tick(self):
        """
        Starts the game.
        User is choosing if he wants to clear levels in file user_levels.json
        If another file was given to the programme as an argument,
        it refers to this file
        """
        print(f"User levels are stored in {self._user_level_path}")
        new_game = input(
            "Do you want to clear existing levels " +
            "in file with user levels?[y/n] "
            )
        try:
            if yes_or_no_answer(new_game):
                with open(self._user_level_path) as f:
                    data = json.load(f)
                data["created_by_user"].clear()
                with open(self._user_level_path, "w") as f:
                    json.dump(data, f, indent=2)
                return self.menu()
            else:
                return self.menu()
        except Exception as e:
            print(e)
            print("Levels have not been cleared!")
            return self.menu()

    def menu(self):
        """
        It is base of the interface,
        it prints all the options
        """
        print(options)
        try:
            data = get_user_input()
        except InvalidInputError as e:
            print(e)
            return self.menu()
        if data == "1":
            self.difficulty()
        elif data == "2":
            self.play_level_added_by_user()
        elif data == "3":
            self.add_level()
        elif data == "4":
            return

    def difficulty(self):
        """
        Allows user to choose a difficulty level,
        If option is invalid user is coming back to the MENU
        """
        print(choose_difficulty())
        try:
            level = get_user_input()
        except InvalidInputError as e:
            print(e)
            return self.menu()
        if level == "1":
            return self.play_easy()
        elif level == "2":
            return self.play_medium()
        elif level == "3":
            return self.play_hard()
        elif level == "4":
            return self.menu()

    def play_easy(self):
        """
        Picks random level from easy levels list and lets user play it.
        If there are no easy levels user is coming back to the Menu
        """
        if len(self._easy_levels) == 0:
            print("There are not any easy levels!")
            return self.menu()
        copy_of_levels = copy.copy(self._easy_levels)
        while len(copy_of_levels) > 0:
            current_level = roll_random_level(copy_of_levels)
            if_correct = play_one_level(current_level)
            if if_correct:
                print("Correct!")
                copy_of_levels.remove(current_level)
            else:
                print("Wrong!")
            playing_again = input("Do you want to play again? [y/n] ")
            try:
                if yes_or_no_answer(playing_again):
                    continue
                else:
                    return self.menu()
            except InvalidInputError as e:
                print(e)
                return self.menu()
        print("You have finished all easy levels!")
        answer = input("Do you want to change difficulty?[y/n] ")
        try:
            if yes_or_no_answer(answer):
                return self.difficulty()
            else:
                return self.play_easy()
        except InvalidInputError as e:
            print(e)
            return self.menu()

    def play_medium(self):
        """
        Picks random level from medium levels list and lets user play it.
        If there are no easy levels user is coming back to the Menu
        """
        if len(self._medium_levels) == 0:
            print("There are not any medium levels!")
            return self.menu()
        copy_of_levels = copy.copy(self._medium_levels)
        while len(copy_of_levels) > 0:
            current_level = roll_random_level(copy_of_levels)
            if_correct = play_one_level(current_level)
            if if_correct:
                print("Correct!")
                copy_of_levels.remove(current_level)
            else:
                print("Wrong!")
            playing_again = input("Do you want to play again? [y/n] ")
            try:
                if yes_or_no_answer(playing_again):
                    continue
                else:
                    return self.menu()
            except InvalidInputError as e:
                print(e)
                return self.menu()
        print("You have finished all medium levels!")
        answer = input("Do you want to change difficulty?[y/n] ")
        try:
            if yes_or_no_answer(answer):
                return self.difficulty()
            else:
                return self.play_medium()
        except InvalidInputError as e:
            print(e)
            return self.menu()

    def play_hard(self):
        """
        Picks random level from hard levels list and lets user play it.
        If there are no easy levels user is coming back to the Menu
        """
        if len(self._hard_levels) == 0:
            print("There are not any hard levels!")
            return self.menu()
        copy_of_levels = copy.copy(self._hard_levels)
        while len(copy_of_levels) > 0:
            current_level = roll_random_level(copy_of_levels)
            if_correct = play_one_level(current_level)
            if if_correct:
                print("Correct!")
                copy_of_levels.remove(current_level)
            else:
                print("Wrong!")
            playing_again = input("Do you want to play again? [y/n] ")
            try:
                if yes_or_no_answer(playing_again):
                    continue
                else:
                    return self.menu()
            except InvalidInputError as e:
                print(e)
                return self.menu()
        print("You have finished all hard levels!")
        answer = input("Do you want to change difficulty?[y/n] ")
        try:
            if yes_or_no_answer(answer):
                return self.difficulty()
            else:
                return self.play_hard()
        except InvalidInputError as e:
            print(e)
            return self.menu()

    def add_level(self):
        """
        Allows user to create his own level.
        If equation given by user is valid,
        programme can write it to file with user levels
        """
        print(instructions)
        try:
            equation = input("Please type in your equation: ")
            check_equation(equation)
            answers = user_creates_his_equation(equation)
        except Exception as e:
            print(e)
            print("You cannot add a level like that!\n")
            return self.menu()

        appending = input(
            "Are you sure you want to add this level to the game?[y/n] "
            )
        try:
            if yes_or_no_answer(appending):
                level = {
                    "equation": equation,
                    "task": "Move one match to make the equation correct",
                    "first_move": answers[0],
                    "second_move": answers[1]
                }
                with open(self._user_level_path) as f:
                    data = json.load(f)
                data["created_by_user"].append(level)
                with open(self._user_level_path, "w") as f:
                    json.dump(data, f, indent=2)
                print(
                    "Great! You added your own level!\n"
                    "Now you can find it in " +
                    "'Play levels created by the user'section\n"
                )
            return self.menu()
        except Exception as e:
            print(e)
            return self.menu()

    def play_level_added_by_user(self):
        """
        Allows to play levels from file diffrent than levels.json
        """
        with open(self._user_level_path) as f:
            data = read_user_levels_from_jason(f)
        if len(data) == 0:
            print("You have to create level first!\n")
            return self.menu()
        else:
            current_level = roll_random_level(data)
            if_correct = play_one_level(current_level)
            if if_correct:
                print("Correct!")
            else:
                print("Wrong")
            option = input("Do you want to play again?[y/n] ")
            try:
                if yes_or_no_answer(option):
                    return self.play_level_added_by_user()
                else:
                    return self.menu()
            except InvalidInputError as e:
                print(e)
                return self.menu()
