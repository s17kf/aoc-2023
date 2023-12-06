#!/usr/bin/env python3

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix


def do_task1(lines):
    list_of_values = [line.split(":")[1] for line in lines]
    points = []
    for values in list_of_values:
        wining, my = values.split("|")
        wining = set(wining.split())
        my = set(my.split())
        my_wining = wining & my
        my_wining_count = len(my_wining)
        if my_wining_count > 0:
            points.append(2 ** (my_wining_count - 1))
    return sum(points)


def do_task2(lines):
    pass


input_lines = common.init_day(4)
if input_lines is None:
    exit(1)

result1 = do_task1(input_lines)
result2 = do_task2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
