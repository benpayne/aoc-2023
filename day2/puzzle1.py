import re

sum = 0

# 12 red cubes, 13 green cubes, and 14 blue cubes
def check_round(round):
    if 'red' in round and round['red'] > 12:
        return False
    elif 'green' in round and round['green'] > 13:
        return False
    elif 'blue' in round and round['blue'] > 14:
        return False
    else:
        return True


with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        parts = re.match(r'^Game (\d*): (.*)$', line)
        game = int(parts[1])
        moves = parts[2].split('; ')
        print(f"{game} ::: {moves}")
        valid = True
        for move in moves:
            round = {}
            move_parts = move.split(', ')
            for part in move_parts:
                match = re.match(r'^(\d*) (red|blue|green)', part)
                #print(match)
                round[match[2]] = int(match[1])
            print(round)
            if not check_round(round):
                valid = False
                break
        if valid:
            sum += game
            


print(f"Total is {sum}")
