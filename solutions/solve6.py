#!/usr/bin/env python3

import common
import numpy
from datetime import datetime


def count_better_times(t, d):
    result = 0
    for current_time in range(t):
        current_distance = current_time * (t - current_time)
        if current_distance > d:
            result += 1
    return result


def do_part1(times, distances):
    times = [int(t) for t in times]
    distances = [int(d) for d in distances]
    print(times)
    print(distances)

    better_times_counters = []
    for i, t in enumerate(times):
        distance = distances[i]
        better_times_counter = count_better_times(t, distance)
        better_times_counters.append(better_times_counter)
    return numpy.prod(better_times_counters)


def do_part2(times, distances):
    full_time = full_distance = ""
    for i, t in enumerate(times):
        full_time += t
        full_distance += distances[i]
    full_time = int(full_time)
    full_distance = int(full_distance)
    return count_better_times(full_time, full_distance)


input_lines = common.init_day(6)
if input_lines is None:
    exit(1)

times, distances = [line.split()[1:] for line in input_lines]

start1 = datetime.now()
result1 = do_part1(times, distances)
time1 = datetime.now() - start1
print(f"task1: {result1}")
print(f"Time 1: {time1}")

start2 = datetime.now()
result2 = do_part2(times, distances)
time2 = datetime.now() - start2
print(f"task2: {result2}")
print(f"Time 2: {time2}")
