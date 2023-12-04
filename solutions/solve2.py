#!/usr/bin/env python3

import common
import numpy

CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_possible(words):
    for i in range(0, len(words), 2):
        value = int(words[i])
        color = words[i + 1]
        if value > CUBES[color]:
            return False
    return True


def get_possible_games(lines):
    possible_games = []
    for line in lines:
        game, results = line.split(": ")
        game_id = int(game.split()[1])
        results = results.replace(";", "")
        results = results.replace(",", "")
        words = results.split()
        if not is_possible(words):
            continue
        possible_games.append(game_id)
    return possible_games


def find_minimum_sets(lines):
    powers = []
    for line in lines:
        _, results = line.split(": ")
        minimum = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        results = results.replace(";", "")
        results = results.replace(",", "")
        words = results.split()
        for i in range(0, len(words), 2):
            value = int(words[i])
            color = words[i + 1]
            minimum[color] = max(minimum[color], value)
        powers.append(numpy.prod([minimum["red"], minimum["green"], minimum["blue"]]))
    return powers


input_lines = common.init_day(2)
if input_lines is None:
    exit(1)

result1 = sum(get_possible_games(input_lines))
result2 = sum(find_minimum_sets(input_lines))

print(f"task1: {result1}")
print(f"task2: {result2}")
