#!/usr/bin/env python3
from _ast import cmpop

import common
from enum import Enum, auto
from collections import Counter
from functools import cmp_to_key
import numpy
from common import numpy_matrix

STRENGTH_OF_A = 15
LABELS = "AKQJT98765432"
FIVE = "FIVE"
FOUR = "FOUR"
FULL = "FULL_HOUSE"
THREE = "THREE"
TWO_PAIR = "TWO_PAIR"
PAIR = "PAIR"
ONE = "ONE_CARD"
HANDS_ORDERED = [FIVE, FOUR, FULL, THREE, TWO_PAIR, PAIR, ONE]


def create_labels_strength_dict():
    strength_dict = dict()
    for i, label in enumerate(LABELS):
        strength_dict[label] = STRENGTH_OF_A - i
    return strength_dict


def create_hands_strength_dict():
    strength_dict = dict()
    max_strength = len(HANDS_ORDERED)
    for i, hand in enumerate(HANDS_ORDERED):
        strength_dict[hand] = max_strength - i
    return strength_dict


HANDS_STRENGTH_DICT = create_hands_strength_dict()


def get_hand_type_strength(hand):
    label_counter = Counter()
    for label in hand:
        label_counter[label] += 1
    most_common = label_counter.most_common(2)
    _, count = most_common[0]
    if count == 5:
        return HANDS_STRENGTH_DICT[FIVE]
    if count == 4:
        return HANDS_STRENGTH_DICT[FOUR]
    _, count_second = most_common[1]
    if count == 3:
        if count_second == 2:
            return HANDS_STRENGTH_DICT[FULL]
        return HANDS_STRENGTH_DICT[THREE]
    if count == 2:
        if count_second == 2:
            return HANDS_STRENGTH_DICT[TWO_PAIR]
        return HANDS_STRENGTH_DICT[PAIR]
    return HANDS_STRENGTH_DICT[ONE]


def compare_hands(hand1, hand2):
    labels_strength_dict = create_labels_strength_dict()
    hand1, _ = hand1.split()
    hand2, _ = hand2.split()
    dif = get_hand_type_strength(hand1) - get_hand_type_strength(hand2)
    if dif != 0:
        return dif
    for i, c1 in enumerate(hand1):
        c2 = hand2[i]
        if c1 == c2:
            continue
        return labels_strength_dict[c1] - labels_strength_dict[c2]
    print("WARNING: Equal hands!")
    return 0


def do_task1(lines):
    lines.sort(key=cmp_to_key(compare_hands))
    winnings = 0
    for i, line in enumerate(lines):
        _, bid = line.split()
        winnings += (i + 1) * int(bid)
    return winnings


def do_task2(lines):
    return "result 2"


input_lines = common.init_day(7)
if input_lines is None:
    exit(1)

result1 = do_task1(input_lines)
result2 = do_task2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
