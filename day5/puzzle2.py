import re

state = 'seeds'
seeds = []
maps = {}

def map_num(map, num):
    for r in map:
        if num >= r['src'] and num < r['src'] + r['length']:
            return r['dest'] + (num - r['src'])
    return num

def map_data(map_name, data):
    results = []
    for d in data:
        num = map_num(maps[map_name], d)
        results.append(num)
        #print(f"{seed} -> {num}")
    return results

with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        #print(line.strip())
        command = re.match(r'([\w-]*) map:$', line)
        if line.startswith('seeds: '):
            seeds = line[7:-1].split(' ')
            #print(seeds)
        elif command:
            #print(f"command {command[1]}")
            state = command[1]
        else:
            data = re.match(r'(\d+) (\d+) (\d+)', line)
            if data:
                #print(f"data {data[1]} {data[2]} {data[3]}")
                if state in maps:
                    maps[state].append({
                        'dest': int(data[1]),
                        'src': int(data[2]),
                        'length': int(data[3]),
                    })
                else:
                    maps[state] = [{
                        'dest': int(data[1]),
                        'src': int(data[2]),
                        'length': int(data[3]),
                    }]

print(seeds)
print(maps)
seeds_array = []
min = -1

for start, length in zip(seeds[::2], seeds[1::2]):
    print(f"{start} {length}")
    for i in range(int(length)):
        results = map_num(maps['seed-to-soil'], int(start) + i)
        results = map_num(maps['soil-to-fertilizer'], results)
        results = map_num(maps['fertilizer-to-water'], results)
        results = map_num(maps['water-to-light'], results)
        results = map_num(maps['light-to-temperature'], results)
        results = map_num(maps['temperature-to-humidity'], results)
        results = map_num(maps['humidity-to-location'], results)
        if min == -1 or results < min:
            min = results

print(f"min location number is {min}") 
