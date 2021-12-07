# Day 2 Part 1
f = "AoC2021/part2.txt"
pos = 0
depth = 0
with open(f, 'r') as data:
    for i in data:
        move = i.strip().split(" ")
        if 'forward' in move[0]:
            pos += int(move[1])
        if 'down' in move[0]:
            depth += int(move[1])
        if 'up' in move[0]:
            depth -= int(move[1])
print(f"D2P1: {pos * depth}")

# Day 2 Part 2
aim = 0
depth = 0
pos = 0
with open(f, 'r') as data:
    for i in data:
        move = i.strip().split(" ")
        if 'forward' in move[0]:
            pos += int(move[1])
            depth += int(move[1]) * aim
        if 'down' in move[0]:
            aim += int(move[1])
        if 'up' in move[0]:
            aim -= int(move[1])
print(f"D2P2: {pos * depth}")