grid = []
with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        grid.append(list(line.strip()))

width = len(grid[0])
height = len(grid)

def get_number(grid, row, col):
    number = 0
    if grid[row][col] == '.':
        return 0
    
    # find start of number
    while col >= 0 and grid[row][col].isdigit():
        col -= 1
    col += 1
    #print(f"Found start at {row} {col}")
    while col < width and grid[row][col].isdigit():
        number = number * 10 + int(grid[row][col])
        col += 1
    print(f"Found number {number}")
    return number

def find_partnum_row(grid, row, col):
    cells = grid[row][col-1:col+2]
    sum = 0
    if cells[1] == '.':
        sum += get_number(grid, row, col-1)
        sum += get_number(grid, row, col+1)
    else:
        sum += get_number(grid, row, col)
    return sum

def find_partnum(grid, row, col):
    sum = 0
    sum += find_partnum_row(grid, row-1, col)
    sum += find_partnum_row(grid, row+1, col)
    sum += get_number(grid, row, col-1)
    sum += get_number(grid, row, col+1)
    return sum

sum = 0
for row, rval in enumerate(grid):
    for col, cell in enumerate(rval):
        if not cell.isdigit() and cell != '.':
            print(f"Found part {cell} at {row} {col}")
            sum += find_partnum(grid, row, col)

print(f"Total is {sum}")