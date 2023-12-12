import argparse
from functools import cmp_to_key

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

hands = []

with open(input_file, 'r') as f:
    data = f.readlines()
    for line in data:
        parts = line.split(" ")
        hand = { 'cards': parts[0], 'bid': parts[1].strip() }
        hands.append(hand)


def hand_type(hand):
    counts = {}
    for card in hand['cards']:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    found_three = False
    found_pair = 0
    for card, count in counts.items():
        if count == 5:
            return 7
        elif count == 4:
            return 6
        elif count == 3:
            found_three = True
        elif count == 2:
            found_pair += 1

    if found_three and found_pair > 0:
        return 5
    elif found_three:
        return 4
    elif found_pair == 2:
        return 3
    elif found_pair == 1:
        return 2
    else:
        return 1
        

def hand_type_p2(hand):
    counts = {}
    for card in hand['cards']:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    found_three = False
    found_pair = 0
    found_wild = counts['J']  if 'J' in counts else 0
    #print(f"Found three {found_three} pair {found_pair} wild {found_wild}")
    if found_wild >= 4: 
        return 7
    for card, count in counts.items():
        if card != 'J':
            if count + found_wild == 5:
                return 7
            elif count + found_wild == 4:
                return 6
            elif count == 3:
                found_three = True
            elif count == 2:
                found_pair += 1

    if found_three:
        if found_wild > 0:
            return 6
        elif found_pair > 0:
            return 5
        else:
            return 4
    elif found_pair == 2:
        if found_wild > 0:
            return 5
        else:   
            return 3
    elif found_pair == 1:
        if found_wild >= 2:
            return 6
        elif found_wild == 1:
            return 4
        else:
            return 2
    else:
        if found_wild >= 2:
            return 4
        elif found_wild == 1:
            return 2
        else:
            return 1

def card_value(card):
    if card >= '2' and card <= '9':
        return int(card)
    elif card == 'T':
        return 10
    elif card == 'J':
        if PUZZLE == 2:
            return 1
        else:
            return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14
    else:
        raise Exception(f"Unknown card {card}")


def compare_hands(hand1, hand2):
    if PUZZLE == 2:
        hand1_type = hand_type_p2(hand1)
        hand2_type = hand_type_p2(hand2)
    else:
        hand1_type = hand_type(hand1)
        hand2_type = hand_type(hand2)
    if hand1_type > hand2_type:
        #print(f"{hand1} > {hand2}")
        return 1
    elif hand1_type < hand2_type:
        #print(f"{hand1} < {hand2}")
        return -1
    else:
        for i in range(5):
            if card_value(hand1['cards'][i]) > card_value(hand2['cards'][i]):
                #print(f"type equal {hand1} > {hand2}")
                return 1
            elif card_value(hand1['cards'][i]) < card_value(hand2['cards'][i]):
                #print(f"type equal {hand1} < {hand2}")
                return -1
        
        #print(f"{hand1} == {hand2}")
        return 0

sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

print(sorted_hands)

sum = 0
for i, hand in enumerate(sorted_hands):
    sum += (i + 1) * int(hand['bid'])

print(f"Sum is {sum}")

#for i, hand in enumerate(sorted_hands):
#    print(f"{i+1} {hand['cards']} {hand['bid']} {hand_type_p2(hand)}")

#print(f"Test JJJJJ 1 {hand_type_p2({'cards': 'JJJJJ', 'bid': '1'})}")
#print(f"Test J2345 2 {hand_type_p2({'cards': 'J2345', 'bid': '2'})}")
#print(f"Test JJ222 3 {hand_type_p2({'cards': 'JJ222', 'bid': '3'})}")
