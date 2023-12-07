#!/usr/bin/env python3

import common


def count_wining_numbers(card):
    wining, my = card.split("|")
    return len(set(wining.split()) & set(my.split()))


def do_task1(lines):
    list_of_values = [line.split(":")[1] for line in lines]
    points = []
    for card in list_of_values:
        won_count = count_wining_numbers(card)
        if won_count > 0:
            points.append(2 ** (won_count - 1))
    return sum(points)


def do_task2(lines):
    list_of_values = [line.split(":")[1] for line in lines]
    instances = [1] * len(lines)
    for i, card in enumerate(list_of_values):
        won_count = count_wining_numbers(card)
        for j in range(won_count):
            instances[i + j + 1] += instances[i]
    return sum(instances)


input_lines = common.init_day(4)
if input_lines is None:
    exit(1)

result1 = do_task1(input_lines)
result2 = do_task2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
