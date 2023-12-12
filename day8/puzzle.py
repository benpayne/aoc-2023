import argparse
import re
import numpy as np

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
    if PUZZLE == 2:
        input_file = 'test2.txt'
    else:
        input_file = 'test.txt'
else:
    input_file = 'input.txt'

direction = None
nodes = {}
with open(input_file, 'r') as f:
    data = f.readlines()
    direction = list(data[0].strip())
    for line in data[2:]:
        m = re.match(r'(\w+) = \((\w+), (\w+)\)', line.strip())
        nodes[m[1]] = [m[2], m[3]]

print(direction)
node_names = []
if PUZZLE == 1:
    node_names = ['AAA']
else:
    node_names = []
    for node_name, node in nodes.items():
        if node_name[2] == 'A':
            node_names.append(node_name)

def test_node_name(node_name):
    if PUZZLE == 2:
        return node_name[2] == 'Z'
    else:
        return node_name == 'ZZZ'

print(f"start - {node_names}")

results = []
for i, node_name in enumerate(node_names):
    dir_i = 0
    while test_node_name(node_name) == False:
        dir = direction[dir_i%len(direction)]
        if dir == 'R':
            node_name = nodes[node_name][1]
        else:
            node_name = nodes[node_name][0]
        dir_i += 1

    results.append(dir_i)

print(results)

print(np.lcm.reduce(results))

