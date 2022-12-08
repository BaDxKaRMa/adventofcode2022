#!/usr/bin/env python3

try:
    with open("day8.txt") as f:
        data = f.read().splitlines()
except FileNotFoundError:
    print("Input file not found")

SAMPLE_INPUT = [
    "stuff",
]
