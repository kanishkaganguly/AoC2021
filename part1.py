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