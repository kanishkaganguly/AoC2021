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
marked = {i:[] for i in range(len(boards))}
