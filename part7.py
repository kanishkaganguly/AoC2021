from dataclasses import dataclass

filepath = 'AoC2021/part7.txt'
# filepath = 'AoC2021/test.txt'
data = []
with open(filepath) as f:
	data = [int(x) for x in f.readline().split(',')]

min_align = 0
max_align = max(data)

class position(object):
	def __init__(self, pos):
		self.pos = pos
		self.distances = []
	def __repr__(self):
		return f"Position:{self.pos} Distances:{self.distances}"
	def __str__(self):
		return f"Position:{self.pos} Distances:{self.distances}"

all_positions = [position(i) for i in data]

for pos in all_positions:
	pos.distances = [abs(pos.pos - i) for i in range(min_align, max_align+1)]

idx_sum = [sum(x) for x in zip(*[d.distances for d in all_positions])]
idx = idx_sum.index(min(idx_sum))
print(f"D7P1: {min(idx_sum)}")

# Day 7 Part 2
def fuel(start, end):
	sum_fuel = 0
	for i in range(abs(start-end)):
		sum_fuel += i+1
	return sum_fuel

all_positions = [position(i) for i in data]

for pos in all_positions:
	pos.distances = [fuel(pos.pos, i) for i in range(min_align, max_align)]

# for p in all_positions:
# 	print(f'{p.pos}: {[str(x).zfill(3) for x in p.distances]}')

idx_sum = [sum(x) for x in zip(*[d.distances for d in all_positions])]
idx = idx_sum.index(min(idx_sum))

print(f"D7P2: {min(idx_sum)}")