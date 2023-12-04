#!/usr/bin/env python3

import common
from enum import Enum, auto
from collections import Counter


CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_possible(sets):
    for cubes_set in sets:
        cubes = cubes_set.split(", ")
        for cube in cubes:
            count, color = cube.split(" ")
            count = int(count)
            if count > CUBES[color]:
                return False
    return True


def get_possible_games(lines):
    possible_games = []
    for line in lines:
        game, results = line.split(": ")
        game_id = int(game.split()[1])
        sets = results.split("; ")
        if not is_possible(sets):
            continue
        possible_games.append(game_id)
    return possible_games


input_lines = common.init_day(2)
if input_lines is None:
    exit(1)

result1 = sum(get_possible_games(input_lines))



result2 = 1

print(f"task1: {result1}")
print(f"task2: {result2}")
