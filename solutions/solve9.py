#!/usr/bin/env python3

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix


def get_next_sequence(sequence):
    next_sequence = []
    for i in range(len(sequence) - 1):
        next_sequence.append(sequence[i + 1] - sequence[i])
    return next_sequence


def contains_zeros_only(sequence):
    for number in sequence:
        if number != 0:
            return False
    return True


def find_next_number(line: str):
    sequence = [int(number) for number in line.split()]
    sequences = [sequence]
    while not contains_zeros_only(sequences[-1]):
        sequences.append(get_next_sequence(sequences[-1]))

    sequences[-1].append(0)
    for i in range(len(sequences) - 2, -1, -1):
        sequence = sequences[i]
        next_sequence = sequences[i + 1]
        sequence.append(sequence[-1] + next_sequence[-1])

    return sequences[0][-1]


def do_part1(lines):
    next_numbers = []
    for line in lines:
        next_numbers.append(find_next_number(line))
    return sum(next_numbers)


def do_part2(lines):
    return "part2"


input_lines = common.init_day(9)
if input_lines is None:
    exit(1)

result1 = do_part1(input_lines)
result2 = do_part2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
