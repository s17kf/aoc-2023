#!/usr/bin/env python3

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix

NORTH = "up"
SOUTH = "down"
EAST = "right"
WEST = "left"
ALL_DIRECTIONS = [NORTH, SOUTH, EAST, WEST]


def get_out_direction(in_direction, pipe):
    match pipe:
        case "|":
            if in_direction in [NORTH, SOUTH]:
                return in_direction
        case "-":
            if in_direction in [EAST, WEST]:
                return in_direction
        case "L":
            if in_direction == SOUTH:
                return EAST
            if in_direction == WEST:
                return NORTH
        case "J":
            if in_direction == SOUTH:
                return WEST
            if in_direction == EAST:
                return NORTH
        case "7":
            if in_direction == NORTH:
                return WEST
            if in_direction == EAST:
                return SOUTH
        case "F":
            if in_direction == NORTH:
                return EAST
            if in_direction == WEST:
                return SOUTH
    return None


def find_start_pos(lines):
    for i, line in enumerate(lines):
        if not "S" in line:
            continue
        for j, c in enumerate(line):
            if c == "S":
                return i, j


def get_next_position(row, col, direction: str):
    match direction:
        case "up":
            return row - 1, col
        case "down":
            return row + 1, col
        case "right":
            return row, col + 1
        case "left":
            return row, col - 1
    return None


def get_first_pipe_and_direction(lines):
    start_row, start_col = find_start_pos(lines)
    for direction in ALL_DIRECTIONS:
        row, col = get_next_position(start_row, start_col, direction)
        if get_out_direction(direction, lines[row][col]) is not None:
            return row, col, direction


def do_part1(lines):
    row, col, direction = get_first_pipe_and_direction(lines)
    distance = 1
    while lines[row][col] != "S":
        direction = get_out_direction(direction, lines[row][col])
        row, col = get_next_position(row, col, direction)
        distance += 1
    return distance / 2


def do_part2(lines):
    return "part2"


input_lines = common.init_day(10)
if input_lines is None:
    exit(1)

result1 = do_part1(input_lines)
result2 = do_part2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
