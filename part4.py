# Day 4 Part 1
from functools import lru_cache

class Board:
	def __init__(self, board, board_width=5, board_index=0):
		self.board_width = board_width
		self.board = board
		self.board_index = board_index
		self.marked = [[0 for _ in range(board_width)]
						for _ in range(board_width)]

		self.get_col = lambda board, col_idx: [elem[col_idx] for elem in board]
		self.get_row = lambda board, row_idx: board[row_idx]

	def __repr__(self):
		print_str = ""
		for row in self.board:
			print_str += f"{row}\n"
		print_str += "\n"

		return print_str

	def __str__(self):
		print_str = ""
		for row in self.board:
			print_str += f"{row}\n"
		print_str += "\n"

		return print_str

	@lru_cache
	def isNumInBoard(self, num):
		r, c = -1, -1
		for row_idx, row in enumerate(self.board):
			try:
				c = row.index(num)
				r = row_idx
				return r, c
			except ValueError:
				c = 0
				r = 0
				continue
		c = -1
		r = -1
		return r, c

	def setMarked(self, r, c):
		self.marked[r][c] = 1

	def printMarked(self):
		print_str = ""
		for row in self.marked:
			print_str += f"{row}\n"
		print_str += "\n"
		print(print_str)

	def sumUnmarked(self):
		unmarked_values = [[self.board[row_idx][col_idx] for col_idx, col in enumerate(row) if col == 0] for row_idx, row in enumerate(self.marked)]
		flat_list = [item for sublist in unmarked_values for item in sublist]
		total_unmarked = sum(flat_list)

		return total_unmarked

	def isWin(self):
		# Check rows
		for i in range(self.board_width):
			if all(self.get_row(self.marked, i)):
				return True
		# Check cols
		for i in range(self.board_width):
			if all(self.get_col(self.marked, i)):
				return True

		return False

	@staticmethod
	def ind2sub(ind, ncols):
		if ind > (ncols * ncols) - 1:
			raise ValueError
		(r, c) = divmod(ind, ncols)
		return (r, c)

	@staticmethod
	def sub2ind(ncols, rows, cols):
		return rows * ncols + cols


board_width = 5


def parseNumsAndBoards(filepath):
    nums = []
    boards = []

    data = []
    with open(filepath) as f:
        data = f.readlines()

    nums = [int(x) for x in data[0].strip().split(sep=",")]

    indices = [i for i, x in enumerate(data) if x == "\n"]

    for idx, i in enumerate(indices):
        board_temp = []
        for j in range(1, board_width + 1):
            board_temp.append([
                int(x)
                for x in data[i + j].strip().replace("  ", " ").split(sep=" ")
            ])
        board = Board(board_temp, board_width, idx)
        boards.append(board)

    return nums, boards

nums, boards = parseNumsAndBoards("AoC2021/part4.txt")

win_board = []
last_called = -1

for num in nums:
	for board_idx, board in enumerate(boards):
		r, c = board.isNumInBoard(num)
		if r != -1 and c != -1:
			board.setMarked(r, c)
			# print(f"Found {num} in Board {board_idx} at {r},{c}")

		if board.isWin():
			last_called = num
			win_board.append(board_idx)

	if len(win_board) > 0:
		break

sum_unmarked = boards[win_board[0]].sumUnmarked()
print(f"D4P1: {sum_unmarked*last_called}")

# Day 4 Part 2
win_board = []
last_called = -1

for num in nums:
	for board_idx, board in enumerate(boards):
		r, c = board.isNumInBoard(num)
		if board_idx not in win_board:
			if r != -1 and c != -1:
				board.setMarked(r, c)
			if board.isWin():
				last_called = num
				win_board.append(board_idx)

sum_unmarked = boards[win_board[-1]].sumUnmarked()
print(f"D4P1: {sum_unmarked*last_called}")