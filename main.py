# Day 1 Part 1
f = "AoC2021/part1.txt"
with open(f, 'r') as data:
    prev = 0
    increase = 0
    for i in data:
        curr = int(i)
        if curr > prev:
            increase += 1
        prev = curr
print(f"D1P1: {increase-1}")

# Day 1 Part 2
with open(f, 'r') as data:
    data_list = []
    for i in data:
        data_list.append(int(i))

window_size = 3
window_sum = [
    sum(data_list[i:i + window_size]) for i in range(0, len(data_list))
]
prev = 0
increase = 0
for curr in window_sum:
    if curr > prev:
        increase += 1
    prev = curr
print(f"D1P2: {increase-1}")

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

# Day 3 Part 1
f = "AoC2021/part3.txt"
num_list = []
with open(f, 'r') as data:
    for i in data:
        num_list.append(i)

bin_length = len(num_list[0]) - 1
most_common = [0 for _ in range(bin_length)]

for i in range(bin_length):
    digits_list = [x[i] for x in num_list]
    digits_bin = ''.join(digits_list)

    ones = digits_bin.count("1")
    zeros = digits_bin.count("0")

    most_common[i] = 1 if ones > zeros else 0

most_common = ''.join(str(i) for i in most_common)
gamma = int(most_common, 2)

least_common = ['1' if i == '0' else '0' for i in most_common]
least_common = ''.join(str(i) for i in least_common)
epsilon = int(least_common, 2)

print(f"D3P1: {gamma*epsilon}")

# Day 3 Part 2
from copy import deepcopy

f = "AoC2021/part3.txt"
num_list = []
with open(f, 'r') as data:
    for i in data:
        num_list.append(i.strip())

bin_length = len(num_list[0]) - 1

def get_most_common(bits_list):
    ones = bits_list.count("1")
    zeros = bits_list.count("0")

    return 1 if ones >= zeros else 0

def get_least_common(bits_list):
    ones = bits_list.count("1")
    zeros = bits_list.count("0")

    return 0 if zeros <= ones else 1

def keep_digits_with_value_at_index(nums, index, value_at):
	return [x for x in nums if int(x[index]) == value_at]

''' Oxygen Generator '''
curr_num_list = deepcopy(num_list)
for i in range(bin_length+1):
	digits_list = [x[i] for x in curr_num_list]
	digits_bin = ''.join(digits_list)

	most_common = get_most_common(digits_bin)
	curr_num_list = keep_digits_with_value_at_index(curr_num_list, i, most_common)

	if len(curr_num_list) == 1:
		break
o2 = int(curr_num_list[0], 2)

''' CO2 Scrubber '''
curr_num_list = deepcopy(num_list)
for i in range(bin_length+1):
	digits_list = [x[i] for x in curr_num_list]
	digits_bin = ''.join(digits_list)

	least_common = get_least_common(digits_bin)
	curr_num_list = keep_digits_with_value_at_index(curr_num_list, i, least_common)

	if len(curr_num_list) == 1:
		break
co2 = int(curr_num_list[0], 2)
print(f"D3P2: {o2*co2}")

# Day 4 Part 1
def printBoard(boardArr):
	for row in boardArr:
		print(row)
	print()

def parseNumsAndBoards(filepath):
	nums = []
	boards = []
	board_width = 6

	data = []
	with open(filepath) as f:
		data = f.readlines()
	
	nums = [int(x) for x in data[0].strip().split(sep=",")]

	indices = [i for i, x in enumerate(data) if x == "\n"]
	for i in indices:
		board = []
		for j in range(1,board_width):
			board.append([int(x) for x in data[i+j].strip().replace("  "," ").split(sep=" ")])
		boards.append(board)

	return nums, boards

nums, boards = parseNumsAndBoards("AoC2021/test.txt")
