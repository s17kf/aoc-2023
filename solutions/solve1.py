#!/usr/bin/env python3

import common
import re


def digit_to_int(digit):
    match digit:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return '3'
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
    return digit


def get_numbers(lines, regex):
    numbers = []
    last_digit_regex = ".*(" + regex + ")"
    for line in lines:
        first_digit = digit_to_int(re.search(regex, line).group(0))
        last_digit = digit_to_int(re.search(last_digit_regex, line).group(1))
        numbers.append(int(first_digit + last_digit))
    return numbers


input_lines = common.init_day(1)
if input_lines is None:
    exit(1)

regex1 = "[0-9]"
regex2 = "[0-9]|one|two|three|four|five|six|seven|eight|nine"

numbers1 = get_numbers(input_lines, regex1)
numbers2 = get_numbers(input_lines, regex2)

result1 = sum(numbers1)
result2 = sum(numbers2)

print(f"task1: {result1}")
print(f"task2: {result2}")
