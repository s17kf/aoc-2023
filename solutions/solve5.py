#!/usr/bin/env python3

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix


def make_input_groups(lines, delimiter=''):
    groups = [[]]
    for i, line in enumerate(lines):
        if line == delimiter:
            if i == len(lines) - 1:
                break
            groups.append([])
            continue
        groups[-1].append(line)
    return groups


def get_source_dest_ranges(group):
    group = group[1:]
    source_ranges = []
    dest_ranges = []
    for line in group:
        dest, source, length = [int(value) for value in line.split()]
        # print((source, dest, length))
        source_ranges.append([source, source + length])
        dest_ranges.append([dest, dest+length])
    return source_ranges, dest_ranges


def in_range(seed, _range):
    start, end = _range
    return start <= seed < end


def transform(seed, ranges):
    print(ranges)
    source_ranges, dest_ranges = ranges
    for i, source_range in enumerate(source_ranges):
        if in_range(seed, source_range):
            padding = seed - source_range[0]
            return dest_ranges[i][0] + padding
    return seed


input_lines = common.init_day(5)
if input_lines is None:
    exit(1)

print(input_lines)

input_groups = make_input_groups(input_lines)

groups_ranges = []
for group in input_groups[1:]:
    print(group)
    source_ranges, dest_ranges = get_source_dest_ranges(group)
    groups_ranges.append([source_ranges, dest_ranges])

print(groups_ranges)

seeds = [int(seed) for seed in input_lines[0].lstrip("seds: ").split()]
print(seeds)

transformed_seeds = []
for seed in seeds:
    for ranges in groups_ranges:
        seed = transform(seed, ranges)
    transformed_seeds.append(seed)

print(transformed_seeds)




result1 = min(transformed_seeds)
result2 = 1

print(f"task1: {result1}")
print(f"task2: {result2}")
