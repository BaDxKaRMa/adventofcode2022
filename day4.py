#!/usr/bin/env python3

from utils import _parse_into_list
from re import match, compile

SAMPLE_INPUT = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def compare_ranges(lines):
    part1 = 0
    part2 = 0
    for line in lines:
        left_elf, right_elf = line.split(",")
        L1, L2 = left_elf.split("-")
        R1, R2 = right_elf.split("-")
        L1, L2, R1, R2 = [int(x) for x in [L1, L2, R1, R2]]
        if L1 <= R1 and R2 <= L2 or R1 <= L1 and L2 <= R2:
            part1 += 1
        if not (L2 < R1 or L1 > R2):
            part2 += 1
    return part1, part2


_PATTERN = compile(r"(\d+)-(\d+),(\d+)-(\d+)")
p1, p2 = 0, 0
for line in _parse_into_list("day4.txt"):
    start1, end1, start2, end2 = map(int, match(_PATTERN, line).groups())
    if start1 <= start2 and end1 >= end2 or start1 >= start2 and end1 <= end2:
        p1 += 1
    if start1 <= end2 and end1 >= start2:
        p2 += 1
print(f"Regex why not Part 1: {p1}")
print(f"Regex why not Part 2: {p2}")

part1, part2 = compare_ranges(_parse_into_list("day4.txt"))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
