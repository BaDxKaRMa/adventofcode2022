#!/usr/bin/env python3

SAMPLE_INPUT = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]

try:
    with open("day6.txt") as f:
        INPUT = f.read()
except FileNotFoundError:
    INPUT = SAMPLE_INPUT


def decode(input_string, size):
    for i in range(len(input_string) - size - 1):
        if len(set(input_string[i : i + size])) == size:
            return i + size


if __name__ == "__main__":
    parts = {"part1": 4, "part2": 14}

    for part, size in parts.items():
        if INPUT is SAMPLE_INPUT:
            print(f"Test Cases for {part}:")
            for line in INPUT:
                print(f"{part}: {decode(line, size)}")
            print()
        else:
            print(f"Part {part}: {decode(INPUT, size)}")
