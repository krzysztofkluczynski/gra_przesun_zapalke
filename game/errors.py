class JsonFileError(Exception):
    def __init__(self):
        super().__init__('''
            Cannot open file with levels data.
            Try to run programme in the same location as levels.json file is
        ''')


class InvalidEquationFormatError(Exception):
    def __init__(self, equation):
        super().__init__("Invalid equation format")
        self._equation = equation


class InvalidCharacterUsedError(Exception):
    def __init__(self, equation):
        super().__init__("Invalid character used")
        self.equation = equation


class EquationTooLongError(Exception):
    def __init__(self, equation):
        super().__init__("Equation is too long")
        self.equation = equation


class InputOutOfRange(Exception):
    def __init__(self, input):
        super().__init__("Character out of range")
        self.character = input


class JsonDataErrorInEasy(Exception):
    def __init__(self):
        super().__init__("Error in reading easy levels from json file")


class JsonDataErrorInMedium(Exception):
    def __init__(self):
        super().__init__("Error in reading medium levels from json file")


class JsonDataErrorInHard(Exception):
    def __init__(self):
        super().__init__("Error in reading hard levels from json file")


class JsonDataErrorInUser(Exception):
    def __init__(self):
        super().__init__("Error in reading user levels from json file")


class InvalidInputError(Exception):
    def __init__(self, data):
        super().__init__("Your input is invalid!")
        self.data = data


class NotANumberError(Exception):
    def __init__(self):
        super().__init__("Input is not a number")


class IndexValueError(Exception):
    def __init__(self, index):
        super().__init__("Index not in expected values")
        self.index = index
