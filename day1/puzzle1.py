import re

sum = 0

with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        numbers = re.findall(r'\d', line)
        num = int(numbers[0] + numbers[-1])
        print(f"{str.strip(line)} {numbers[0]} {numbers[-1]} {num}")
        sum += num

print(f"Total is {sum}")