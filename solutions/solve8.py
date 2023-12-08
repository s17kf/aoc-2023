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


def get_network_dict(lines):
    network_dict = dict()
    for line in lines[2:]:
        source, dests = line.split(" = ")
        dests = dests.strip("()").split(", ")
        network_dict[source] = dests
    return network_dict


def do_part1(lines, start_node="AAA", end_condition=lambda node: node == "ZZZ"):
    instructions = lines[0]
    network_dict = get_network_dict(lines)
    node = start_node
    instruction = 0
    steps = 0
    while not end_condition(node):
        steps += 1
        node = network_dict[node][DIR_INDICES[instructions[instruction]]]
        instruction = (instruction + 1) % len(instructions)
    return steps


def do_part2(lines):
    instructions = lines[0]
    network_dict = get_network_dict(lines)
    nodes = []
    for node in network_dict.keys():
        if node[2] == "A":
            nodes.append(node)
    instruction = 0
    steps = 0
    done = False
    while not done:
        # print(f"{steps}: {nodes}")
        steps += 1
        direction = DIR_INDICES[instructions[instruction]]
        instruction = (instruction + 1) % len(instructions)
        for i in range(len(nodes)):
            node = nodes[i]
            nodes[i] = network_dict[node][direction]
        done = True
        for node in nodes:
            if node[2] != "Z":
                done = False
                break
        # if steps == 10:
        #     break
    return steps


input_lines = common.init_day(8)
if input_lines is None:
    exit(1)

result1 = do_part1(input_lines)
print(f"task1: {result1}")

result2 = do_part2(input_lines)
print(f"task2: {result2}")
