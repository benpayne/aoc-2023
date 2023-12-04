import re

sum = 0

cards = {1: 1}

def inc_card(card_index, count):
    if card_index in cards:
        cards[card_index] += count
    else:
        cards[card_index] = count + 1


card = 0

#            0 1 2 3 4 5 6 T
# Card 1: 4  1 0           1
# Card 2: 2  1 1 0         2
# Card 3: 2  1 1 2 0       4
# Card 4: 1  1 1 2 4 0     8
# Card 5: 0  1 1 0 4 8 0   14
# Card 6: 0  1 0 0 0 0 0 0 1
#            6 4 4 8 8 0 0 30

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
        print(f"scrore {len(winning)} with {winning}")
        if card not in cards:
            cards[card] = 1
        for card_idx in range(len(winning)):
            inc_card(card+card_idx+1, cards[card])


print(cards)
for i in range(1,card+1):
    print(f"Card {i} : {cards[i]}")
    sum += cards[i]

print(f"Total is {sum}")
