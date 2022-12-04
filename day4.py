#!/usr/bin/env python3

from utils import _parse_into_list

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


part1, part2 = compare_ranges(_parse_into_list("day4.txt"))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
