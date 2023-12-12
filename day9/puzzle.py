import argparse
import re
#import numpy as np

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('-t', '--test', action='store_true', default=False, help='Use the test input')
parser.add_argument('--puzzle1', action='store_true', default=False, help='Run puzzle 1')
parser.add_argument('--puzzle2', action='store_true', default=False, help='Run puzzle 2')
args = parser.parse_args()

TEST = args.test
PUZZLE = 1
if args.puzzle2:
    PUZZLE = 2

if TEST:
    input_file = 'test.txt'
else:
    input_file = 'input.txt'

sequences = []

with open(input_file, 'r') as f:
    data = f.readlines()
    for line in data:
        seq = [int(x) for x in line.strip().split(' ')]
        sequences.append(seq)

print(sequences)

def not_all_zeros(sequence):
    for num in sequence:
        if num != 0:
            return True
    return False

def run_difference(sequence):
    print(f"result: {sequence}")

    if not_all_zeros(sequence):
        result = []
        prev = sequence[0]
        for num in sequence[1:]:
            result.append(num - prev)
            prev = num
        lower = run_difference(result)
        print(f"lower: {lower}")
        if PUZZLE == 1:
            sequence.append(sequence[-1] + lower[-1])
        else:
            sequence.insert(0, sequence[0] - lower[0])

    else:
        if PUZZLE == 1:
            sequence.append(0)
        else:
            sequence.insert(0, 0)
    return sequence


sum = 0
for seq in sequences:
    res = seq
    print(f"Sequence: {seq}")
    res = run_difference(seq)
    if PUZZLE == 1:
        sum += res[-1]
    else:
        sum += res[0]
    print(f" {res}")

print(f"Total is {sum}")