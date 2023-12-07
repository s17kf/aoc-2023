#!/usr/bin/env python3

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix


def do_part1(lines):
    print(lines)
    return "part 1"


def do_part2(lines):
    return "part2"


input_lines = common.init_day(DAY_NUM)
if input_lines is None:
    exit(1)

result1 = do_part1(input_lines)
result2 = do_part2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
