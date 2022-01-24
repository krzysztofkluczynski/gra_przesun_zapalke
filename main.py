from game.interface import Interface
from game.levels_io import (
    read_easy_levels_from_json,
    read_medium_levels_from_jason,
    read_hard_levels_from_jason,
    read_user_levels_from_jason
)
from argparse import ArgumentParser
import sys


def _create_parser():
    """
    Creates parser using argparse,
    Adds optional path argument
    """
    parser = ArgumentParser(
        description="Passing user levels to programme"
    )

    parser.add_argument(
        "-path",
        help="path to the file with user levels, not required",
    )
    return parser


def load_user_levels_from_json_file(path: str):
    try:
        with open(path, "r") as handle:
            return read_user_levels_from_jason(handle)
    except Exception as e:
        print(e)
        print(
            "Cannot read levels from given direcotry, " +
            "you will play on user_levels.json file from data directory"
        )
        return False


def main(args):
    try:
        with open("data/levels.json") as f:
            easy_levels = read_easy_levels_from_json(f)
            f.seek(0)
            medium_levels = read_medium_levels_from_jason(f)
            f.seek(0)
            hard_levels = read_hard_levels_from_jason(f)
    except Exception as e:
        print(e)
        return

    parser = _create_parser()
    arguments = parser.parse_args(args)
    path = "data/user_levels.json"
    if arguments.path:
        user_levels = load_user_levels_from_json_file(arguments.path)
        if user_levels is False:
            with open(path) as f:
                user_levels = read_user_levels_from_jason(f)
        else:
            path = arguments.path
    else:
        with open(path) as f:
            user_levels = read_user_levels_from_jason(f)
    try:
        ui = Interface(
            path,
            easy_levels,
            medium_levels,
            hard_levels,
        )
        ui.tick()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main(sys.argv[1:])
