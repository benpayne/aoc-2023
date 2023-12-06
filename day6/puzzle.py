#Time:      7  15   30
#Distance:  9  40  200

import argparse

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('-t', '--test', action='store_true', default=False, help='Use the test input')
parser.add_argument('--puzzle1', action='store_true', default=False, help='Run puzzle 1')
parser.add_argument('--puzzle2', action='store_true', default=False, help='Run puzzle 2')
args = parser.parse_args()

TEST = args.test

test_input_puzzle1 = [
    {'time': 7, 'distance': 9},
    {'time': 15, 'distance': 40},
    {'time': 30, 'distance': 200},
]

test_input_puzzle2 = [
    {'time': 71530, 'distance': 940200},
]


#Time:        58     81     96     76
#Distance:   434   1041   2219   1218

if TEST:
    input_puzzle1 = test_input_puzzle1
    input_puzzle2 = test_input_puzzle2
else:
    input_puzzle1 = [
        {'time': 58, 'distance': 434},
        {'time': 81, 'distance': 1041},
        {'time': 96, 'distance': 2219},
        {'time': 76, 'distance': 1218},
    ]
    input_puzzle2 = [
        {'time': 58819676, 'distance': 434104122191218},
    ]

def time_to_distance(time, max_time):
    distance = 0
    speed = time
    duration = max_time - time
    return speed * duration

def count_scenerios(max_time, best_distance):
    count = 0
    for time in range(1, max_time):
        distance = time_to_distance(time, max_time)
        if distance > best_distance:
            count += 1
    return count    

if args.puzzle2:
    puzzle = 2
else:
    puzzle = 1

if puzzle == 1:
    total = 1
    input = input_puzzle1
else:
    total = 0
    input = input_puzzle2

for i in input:
    res = count_scenerios(i['time'], i['distance'])
    print(f"{i['time']} {i['distance']} {res}")
    if puzzle == 1:
        total *= res
    else:
        total += res

print(f"Product is {total}")