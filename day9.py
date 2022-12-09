#!/usr/bin/env python3
# Day 9 Advent of Code 2022
# https://adventofcode.com/2022/day/9
# Loguru this time

import os
from utils import parse_args, setup_logging

SAMPLE_INPUT = """\
123
"""


def load_input():
    if os.path.exists("day9.txt"):
        with open(os.path.join(os.path.dirname(__file__), "day9.txt")) as f:
            input_data = f.read().splitlines()
            logger.debug(f"Loaded day9.txt: {input_data}")
    else:
        input_data = SAMPLE_INPUT.splitlines()
        logger.debug(f"Loaded sample input: {input_data}")
    return input_data


if __name__ == "__main__":
    # Parse the arguments
    args = parse_args()
    # setup logger
    logger = setup_logging(args.debug)

    # Start here
    data = load_input()
