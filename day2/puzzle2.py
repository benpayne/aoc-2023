import re

class Dice:
    def __init__(self):
        self.color_max = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

    def max(self, color, count):
        if count > self.color_max[color]:
            self.color_max[color] = count

    def power(self) -> int:
        return self.color_max['red'] * self.color_max['green'] * self.color_max['blue']
    

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

sum = 0

with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        parts = re.match(r'^Game (\d*): (.*)$', line)
        game = int(parts[1])
        moves = parts[2].split('; ')
        print(f"{game} ::: {moves}")
        dice = Dice()
        for move in moves:
            move_parts = move.split(', ')
            for part in move_parts:
                match = re.match(r'^(\d*) (red|blue|green)', part)
                #print(f"{match[2]} ::: {match[1]}")
                dice.max(match[2], int(match[1]))
        sum += dice.power()
            


print(f"Total is {sum}")
