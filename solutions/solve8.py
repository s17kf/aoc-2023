#!/usr/bin/env python3

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix

DIR_INDICES = {
    "L": 0,
    "R": 1
}


def do_part1(lines):
    instructions = lines[0]
    network_dict = dict()
    for line in lines[2:]:
        source, dests = line.split(" = ")
        dests = dests.strip("()").split(", ")
        network_dict[source] = dests
    node = "AAA"
    i = 0
    steps = 0
    while node != "ZZZ":
        steps += 1
        node = network_dict[node][DIR_INDICES[instructions[i]]]
        i = (i + 1) % len(instructions)
    return steps


def do_part2(lines):
    return "part2"


input_lines = common.init_day(8)
if input_lines is None:
    exit(1)

result1 = do_part1(input_lines)
result2 = do_part2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
