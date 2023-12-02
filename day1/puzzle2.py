import numpy as np

sum = 0

nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six' : '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        positions = [line.find(k) if line.find(k) != -1 else len(line) for k in nums.keys()]
        rpositions = [line.rfind(k) for k in nums.keys()]
        print(f"{np.argmin(positions)} : {np.argmax(rpositions)}")
        first_str = list(nums.keys())[np.argmin(positions)]
        last_str = list(nums.keys())[np.argmax(rpositions)]
        first = nums[first_str]
        last = nums[last_str]
        num = int(first + last)
        print(f"{str.strip(line)} : {positions} : {first_str} {last_str} {num}")
        sum += num

print(f"Total is {sum}")