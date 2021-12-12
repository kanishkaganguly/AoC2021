from collections import deque

filepath = "AoC2021/part6.txt"

# Day 6 Part 1
all_fish = []
with open(filepath) as f:
	all_fish = [int(x) for x in f.readlines()[0].split(',')]

fish_spawn_duration = 9
fish_spawn_time = deque([0 for i in range(fish_spawn_duration)])
for fish_spawn in all_fish:
	fish_spawn_time[fish_spawn] += 1

days = 80
for day in range(days):
	fish_spawn_time.rotate(-1)
	fish_spawn_time[6] += fish_spawn_time[8]

print(f"D6P1: {sum(fish_spawn_time)}")

# Day 6 Part 2
fish_spawn_time = deque([0 for i in range(fish_spawn_duration)])
for fish_spawn in all_fish:
	fish_spawn_time[fish_spawn] += 1
days = 256
for day in range(days):
	fish_spawn_time.rotate(-1)
	fish_spawn_time[6] += fish_spawn_time[8]

print(f"D6P2: {sum(fish_spawn_time)}")