filepath = "AoC2021/part5.txt"
starts = []
ends = []
with open(filepath) as f:
	for data in f:
		coords = data.strip().split(" -> ")
		start_coord = tuple([int(x) for x in coords[0].split(",")])
		end_coord = tuple([int(x) for x in coords[1].split(",")])
		starts.append(start_coord)
		ends.append(end_coord)

def showVents(vents_table):
	for row in vents_table:
		for col in row:
			if col == 0:
				print(f".", end=" ")
			else:
				print(f"{col}", end=" ")
		print()
	print()

from operator import itemgetter
max_x = max(starts,key=itemgetter(0))[0]
max_y = max(starts,key=itemgetter(1))[1]

vents_table = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

def countOverlap(vents_table):
	total = 0
	[[total:= total + 1 for col in row if col >=2] for row in vents_table]
	return total

def ConditionalRange(start, end):
	if start < end:
		return [i for i in range(start, end+1)]
	else:
		return [i for i in range(start, end-1, -1)]

part2 = True
# Day 5 Part 1
for start, end in zip(starts, ends):
	(startx, starty) = start
	(endx, endy) = end

	if startx == endx:
		for i in ConditionalRange(starty, endy):
			vents_table[i][startx] += 1
	elif starty == endy:
		for i in ConditionalRange(startx, endx):
			vents_table[starty][i] += 1
	else:
		# Day 5 Part 2
		if part2:
			i = ConditionalRange(starty, endy)
			j = ConditionalRange(startx, endx)
			for (x,y) in zip(i, j):
				vents_table[x][y] += 1

print(f"D5P1: {countOverlap(vents_table)}")