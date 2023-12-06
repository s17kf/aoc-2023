#!/usr/bin/env python3

import common
import numpy

NUMBERS = "0123456789"
NOT_SYMBOLS = NUMBERS + "."
STAR = "*"


class Number:
    line_len = 0

    def __init__(self, value, line, start, end):
        self.value = value
        self.line = line
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.value}-[{self.line}:{self.start}-{self.end}]"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.value


def find_all_numbers(lines):
    start = end = 0
    found_numbers = []
    for line_num, line in enumerate(lines):
        for i, c in enumerate(line):
            if c in NUMBERS:
                if i == 0 or line[i - 1] not in NUMBERS:
                    start = i
                    if i != len(line) - 1 and line[i + 1] in NUMBERS:
                        continue
                if i == len(line) - 1 or line[i + 1] not in NUMBERS:
                    end = i
                    number = Number(int(line[start:end + 1]), line_num, start, end)
                    found_numbers.append(number)
                    continue
    return found_numbers


def get_begin_finish_indices(number: Number):
    begin = number.start - 1 if number.start > 0 else 0
    finish = number.end + 1 if number.end < Number.line_len - 1 else number.end
    return begin, finish


def is_symbol_above(lines, number: Number):
    if number.line == 0:
        return False
    begin, finish = get_begin_finish_indices(number)
    above_area = lines[number.line - 1][begin:finish + 1]
    for c in above_area:
        if c not in NOT_SYMBOLS:
            return True
    return False


def is_symbol_below(lines, number: Number):
    if number.line == len(lines) - 1:
        return False
    begin, finish = get_begin_finish_indices(number)
    below_area = lines[number.line + 1][begin:finish + 1]
    for c in below_area:
        if c not in NOT_SYMBOLS:
            return True
    return False


def is_symbol_left(lines, number: Number):
    if number.start == 0:
        return False
    return lines[number.line][number.start - 1] not in NOT_SYMBOLS


def is_symbol_right(lines, number: Number):
    if number.end == Number.line_len - 1:
        return False
    return lines[number.line][number.end + 1] not in NOT_SYMBOLS


def do_part_day(lines):
    Number.line_len = len(lines[0])
    numbers = find_all_numbers(lines)
    numbers_adjacent_to_symbol = []
    for number in numbers:
        if is_symbol_above(input_lines, number) or is_symbol_below(input_lines, number) or \
                is_symbol_left(input_lines, number) or is_symbol_right(input_lines, number):
            numbers_adjacent_to_symbol.append(int(number))
    stars = find_all_stars(lines)
    ratios = []
    for star in stars:
        ratios.append(get_ratio(lines, star[0], star[1]))
    return sum(numbers_adjacent_to_symbol), sum(ratios)


def get_number(line, i):
    start = end = i
    while start > 0 and line[start - 1] in NUMBERS:
        start -= 1
    while end < len(line) - 1 and line[end + 1] in NUMBERS:
        end += 1
    return int(line[start:end + 1])


def get_adjacent_numbers_for_gear_in_line(line, i, gear_in_line=False):
    if not gear_in_line and line[i] in NUMBERS:
        return [get_number(line, i)]
    if i > 0 and line[i - 1] in NUMBERS:
        if i < len(line) - 1 and line[i + 1] in NUMBERS:
            return [get_number(line, i - 1), get_number(line, i + 1)]
        return [get_number(line, i - 1)]
    if i < len(line) - 1 and line[i + 1] in NUMBERS:
        return [get_number(line, i + 1)]
    return []


def get_ratio(lines, line_num, i):
    adjacent_numbers = []
    if line_num > 0:
        for number in get_adjacent_numbers_for_gear_in_line(lines[line_num - 1], i):
            adjacent_numbers.append(number)
    if line_num < len(lines) - 1:
        for number in get_adjacent_numbers_for_gear_in_line(lines[line_num + 1], i):
            adjacent_numbers.append(number)
    for number in get_adjacent_numbers_for_gear_in_line(lines[line_num], i, True):
        adjacent_numbers.append(number)
    if len(adjacent_numbers) == 2:
        return numpy.prod(adjacent_numbers)
    return 0


def find_all_stars(lines):
    stars = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == STAR:
                stars.append([i, j])
    return stars


input_lines = common.init_day(3)
if input_lines is None:
    exit(1)

result1, result2 = do_part_day(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
