import argparse
import re
#import numpy as np
import copy
from io import StringIO

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

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.row_expand = []
        self.col_expand = []

    def get(self, r, c):
        if r < 0 or r >= self.height or c < 0 or c >= self.width:
            return None
        return self.grid[r][c]

    def set(self, r, c, value):
        self.grid[r][c] = value

    def insert_row(self, r, row):
        self.grid.insert(r, row)
        self.height += 1

    def insert_col(self, c, col):
        for r, row in enumerate(self.grid):
            row.insert(c, col[r])
        self.width += 1

    def get_row(self, r):
        return self.grid[r]
    
    def get_col(self, c):
        return [row[c] for row in self.grid]
    
    def expand_row(self, r, times):
        self.row_expand.append((r, times))

    def expand_col(self, c, times):
        self.col_expand.append((c, times))

    def expand_cordinate(self, r, c):
        added_r = 0
        added_c = 0
        for col, times in self.col_expand:
            if c >= col:
                #print(f"Expanding col {col} by {times}")
                added_c += times
        for row, times in self.row_expand:
            if r >= row:
                #print(f"Expanding row {row} by {times}")
                added_r += times
        return r + added_r, c + added_c

    def find_all(self, value):
        found = []
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == value:
                    found.append((r, c))
        return found
    
    def __str__(self):
        output = StringIO()
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                output.write(f"{self.grid[r][c]}")
            output.write("\n")
        return output.getvalue()

input = []
with open(input_file, 'r') as f:
    data = f.readlines()
    for i, line in enumerate(data):
        input.append(list(line.strip()))

grid = Grid(input)

def expand_grid(grid):
    if PUZZLE == 1:
        expand = 1
    else:
        expand = 999999

    def all_space(row):
        for cell in row:
            if cell != '.':
                return False
        return True

    for i in range(grid.height):
        print(f"Checking row {i}")
        row = grid.get_row(i)
        if all_space(row):
            grid.expand_row(i, expand)
            print(f"Inserting row {i}")

    for i in range(grid.width):
        print(f"Checking col {i}")
        col = grid.get_col(i)
        if all_space(col):
            grid.expand_col(i, expand)
            print(f"Inserting col {i}")

print(grid)
expand_grid(grid)
print(grid)

locations = grid.find_all('#')

sum = 0
for i, start in enumerate(locations):
    for loc in locations[i+1:]:
        estart = grid.expand_cordinate(start[0], start[1])
        eloc = grid.expand_cordinate(loc[0], loc[1])
        distance = abs(estart[0] - eloc[0]) + abs(estart[1] - eloc[1])
        sum += distance

print(f"Total is {sum}")

#print(f"{grid.expand_cordinate(6,9)}")