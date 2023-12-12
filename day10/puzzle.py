import argparse
import re
#import numpy as np
import copy

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

grid = []
with open(input_file, 'r') as f:
    data = f.readlines()
    for i, line in enumerate(data):
        grid.append(list(line.strip()))
        if 'S' in line:
            start = (i, line.index('S'))

print(grid)
print(start)

def find_start(grid, cell):
    r, c = cell
    adjacent = []
    if c+1 < len(grid[r]) and (grid[r][c+1] == '-' or grid[r][c+1] == 'J' or grid[r][c+1] == '7'):
        adjacent.append('E')
    if c>0 and (grid[r][c-1] == '-' or grid[r][c-1] == 'L' or grid[r][c-1] == 'F'):
        adjacent.append('W')
    if r+1 < len(grid) and (grid[r+1][c] == '|' or grid[r+1][c] == 'J' or grid[r+1][c] == 'L'):
        adjacent.append('S')
    if r>0 and (grid[r-1][c] == '|' or grid[r-1][c] == 'F' or grid[r-1][c] == '7'):
        adjacent.append('N')

    if 'S' in adjacent and 'N' in adjacent:
        grid[r][c] = '|'
        return r+1, c
    elif 'S' in adjacent and 'E' in adjacent:
        grid[r][c] = 'F'
        return r, c+1
    elif 'S' in adjacent and 'W' in adjacent:
        grid[r][c] = '7'
        return r, c-1
    elif 'N' in adjacent and 'E' in adjacent:
        grid[r][c] = 'L'
        return r, c+1
    elif 'N' in adjacent and 'W' in adjacent:
        grid[r][c] = 'J'
        return r, c-1
    elif 'E' in adjacent and 'W' in adjacent:
        grid[r][c] = '-'
        return r, c+1
    else:
        raise Exception(f"Bad start {adjacent}")


def walk(grid, cell, prev, value):
    r, c = cell
    pr, pc = prev
    pipe = grid[r][c]
    grid[r][c] = value
    prev_dir = None
    dir = None
    if r == pr:
        if c > pc:
            prev_dir = 'W'
        else:
            prev_dir = 'E'
    else:
        if r > pr:
            prev_dir = 'N'
        else:
            prev_dir = 'S'

    print(f"prev {prev} cell {cell} prev_dir {prev_dir} pipe {pipe}")

    if pipe == 'J':
        if prev_dir == 'N':
            dir = 'W'
        elif prev_dir == 'W':
            dir = 'N'
        else:
            raise Exception("Bad J")
    elif pipe == 'L':
        if prev_dir == 'N':
            dir = 'E'
        elif prev_dir == 'E':
            dir = 'N'
        else:
            raise Exception("Bad L")
    elif pipe == 'F':
        if prev_dir == 'S':
            dir = 'E'
        elif prev_dir == 'E':
            dir = 'S'
        else:
            raise Exception("Bad F")
    elif pipe == '7':
        if prev_dir == 'S':
            dir = 'W'
        elif prev_dir == 'W':
            dir = 'S'
        else:
            raise Exception("Bad 7")
    elif pipe == '|':
        if prev_dir == 'N':
            dir = 'S'
        elif prev_dir == 'S':
            dir = 'N'
        else:
            raise Exception("Bad |")
    elif pipe == '-':
        if prev_dir == 'E':
            dir = 'W'
        elif prev_dir == 'W':
            dir = 'E'
        else:
            raise Exception("Bad -")
    elif pipe == 'S':
        return None
    else:
        raise Exception(f"Bad pipe {pipe}")
    
    if dir == 'N':
        return r-1, c
    elif dir == 'S':
        return r+1, c
    elif dir == 'E':
        return r, c+1
    elif dir == 'W':
        return r, c-1
    else:
        raise Exception(f"Bad dir {dir}")

def dump_grid(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            print(f"{grid[r][c]:4}", end='')
        print()

# walk loop
sum = 0
next = find_start(grid, start)
dump_grid(grid)
grid_path = copy.deepcopy(grid)
grid_path[start[0]][start[1]] = 0
prev = start
while next != start:
    print(f"next {next} prev {prev}")
    sum += 1
    save = next
    next = walk(grid_path, next, prev, sum)
    prev = save

dump_grid(grid_path)

print(f"Total is {(sum+1)/2}")

sum = 0
if PUZZLE == 2:
    for r, row in enumerate(grid_path):
        inside = False
        for c, cell in enumerate(row):
            if isinstance(cell, int):
                pipe = grid[r][c]
                if pipe == '|':
                    inside = not inside
                elif pipe == 'F' or pipe == 'L':
                    start = pipe
                elif pipe == '7' or pipe == 'J':
                    if not ((start == 'F' and pipe == '7') or 
                            (start == 'L' and pipe == 'J')): 
                        inside = not inside
                elif pipe == '-':
                    pass
                else:
                    raise Exception(f"Bad pipe {pipe}")

                print(grid[r][c], end='')
            else:
                if inside:
                    print('X', end='')
                    sum+=1
                else:
                    print(' ', end='')

        print()

print(f"Total inside {sum}")
