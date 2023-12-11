#!/usr/bin/env python3

import common


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


def generate_helper_sequences(first_sequence):
    sequences = [first_sequence]
    while not contains_zeros_only(sequences[-1]):
        sequences.append(get_next_sequence(sequences[-1]))
    return sequences


def extrapolate_sequences(sequences, new_value_function):
    for i in range(len(sequences) - 2, -1, -1):
        sequence = sequences[i]
        next_sequence = sequences[i + 1]
        new_value_function(sequence, next_sequence)


def add_sum_to_end(sequence, next_sequence):
    sequence.append(sequence[-1] + next_sequence[-1])


def add_diff_to_beginning(sequence, next_sequence):
    sequence.insert(0, sequence[0] - next_sequence[0])


def extrapolate_line(line, new_value_function, result_getter):
    sequence = [int(number) for number in line.split()]
    sequences = generate_helper_sequences(sequence)

    sequences[-1].append(0)
    extrapolate_sequences(sequences, new_value_function)
    return result_getter(sequences)


def do_part1(lines):
    next_numbers = []
    for line in lines:
        next_numbers.append(extrapolate_line(line, add_sum_to_end, lambda sequences: sequences[0][-1]))
    return sum(next_numbers)


def do_part2(lines):
    prev_numbers = []
    for line in lines:
        prev_numbers.append(extrapolate_line(line, add_diff_to_beginning, lambda sequences: sequences[0][0]))
    return sum(prev_numbers)


input_lines = common.init_day(9)
if input_lines is None:
    exit(1)

result1 = do_part1(input_lines)
result2 = do_part2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
