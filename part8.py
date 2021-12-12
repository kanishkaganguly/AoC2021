filepath = "AoC2021/part8.txt"
signal_patterns = None
output_values = None

data = []
with open(filepath) as f:
	data = f.readlines()
num_lines = len(data)

signal_patterns = [[] for _ in range(num_lines)]
output_values = [[] for _ in range(num_lines)]
for idx, d in enumerate(data):
	parse = d.split(' | ')
	signal_patterns[idx] = parse[0].split(' ')
	output_values[idx] = parse[1].strip().split(' ')

segments = {1:2, 4:4, 7:3, 8:7}

digit_len = [[1 if len(v) in segments.values() else 0 for v in ov] for ov in output_values]
digit_sum = [i for sublist in digit_len for i in sublist].count(1)
print(f"D8P1: {digit_sum}")