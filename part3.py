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