#!/usr/bin/env python3


SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "day19.txt")

SAMPLE_INPUT = """\
Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian."""

try:
    with INPUT_FILE.open() as f:
        lines = f.read().splitlines()
except FileNotFoundError:
    lines = SAMPLE_INPUT.splitlines()
