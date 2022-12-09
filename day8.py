#!/usr/bin/env python3

import numpy as np

try:
    with open("day8.txt") as f:
        data = f.read().splitlines()
except FileNotFoundError:
    print("Input file not found")

SAMPLE_INPUT = """
30373
25512
65332
33549
35390
"""

grid = np.array([list(x.strip()) for x in open("day8.txt")], int)
part1 = np.zeros_like(grid, int)
part2 = np.ones_like(grid, int)

# rotate the grid 90 degrees clockwise 4 times
for _ in range(4):
    for (x, y), _ in np.ndenumerate(grid):
        lower = [t < grid[x, y] for t in grid[x, y + 1 :]]

        if all(lower):
            part1[x, y] = 1
        part2[x, y] *= next((i + 1 for i, t in enumerate(lower) if ~t), len(lower))
    # rotate grid
    grid, part1, part2 = map(np.rot90, [grid, part1, part2])

print(f"Part 1: {part1.sum()}")
print(f"Part 2: {part2.max()}")
