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
    nums = [0, 0]
    if cells[1] == '.':
        nums[0] = get_number(grid, row, col-1)
        nums[1] = get_number(grid, row, col+1)
    else:
        nums[0] += get_number(grid, row, col)
    return nums

def find_partnum(grid, row, col):
    ratio_nums = []
    nums = find_partnum_row(grid, row-1, col)
    if nums[0] != 0:
        ratio_nums.append(nums[0])
    if nums[1] != 0:
        ratio_nums.append(nums[1])
    nums = find_partnum_row(grid, row+1, col)
    if nums[0] != 0:
        ratio_nums.append(nums[0])
    if nums[1] != 0:
        ratio_nums.append(nums[1])
    num = get_number(grid, row, col-1)
    if num != 0:
        ratio_nums.append(num)
    num = get_number(grid, row, col+1)
    if num != 0:
        ratio_nums.append(num)
    return ratio_nums

sum = 0
for row, rval in enumerate(grid):
    for col, cell in enumerate(rval):
        if cell == '*':
            print(f"Found possible gear {cell} at {row} {col}")
            nums = find_partnum(grid, row, col)
            if len(nums) == 2:
                print(f"Found gear {cell} at {row} {col}")
                sum += nums[0] * nums[1]

print(f"Total is {sum}")