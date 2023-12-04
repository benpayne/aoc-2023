import re

sum = 0

with open('input.txt', 'r') as f:
    data = f.readlines()
    pattern = re.compile(r'(\d+)\s*')
    for line in data:
        parts = re.match(r'^Card\s+(\d*): ([^|]*) \| (.*)$', line)
        card = int(parts[1])
        answers = set(pattern.findall(parts[2]))
        guesses = set(pattern.findall(parts[3]))
        print(f"{card} ::: {answers} ::: {guesses}")
        winning = answers.intersection(guesses)
        score = 0
        if len(winning) > 0:
            score = 2 ** (len(winning) - 1)
        print(f"scrore {score} with {winning}")
        sum += score
        
print(f"Total is {sum}")
