#class GameBoard:
#	def __init__ (self):
#	self.rows = 7
#	self.columns = 5

def horizontal (board, state):
	for y in range(columns):
		in_row = 0
		for x in range(rows):
			if (board[x][y] == state):
				in_row = in_row + 1
				if (in_row == 4):
					return true
			else:
				in_row = 0
	return false

def vertical (board, state):
	for x in range(rows):
		in_row = 0
		for y in range(columns):
			if (board[x][y] == state):
				in_row = in_row + 1
				if (in_row == 4):
					return true
			else:
				in_row = 0
	return false

def diag_upright (board, state,x,y):
	in_row = 0
	while(x <= rows and y <= columns):
		if (board[x][y] == state):
			in_rows = in_rows + 1
			if(in_row == 4):
				return true
			x = x + 1
			y = y + 1
		else: 
			in_row = 0
			x = x + 1
			y = y + 1
	return false

def diag_downright (board, state,x,y):
	in_row = 0
	while(x >= 0 and y >= 0):
		if (board[x][y] == state):
			in_rows = in_rows + 1
			if(in_row == 4):
				return true
			x = x - 1
			y = y - 1
		else: 
			in_row = 0
			x = x - 1
			y = y - 1
	return false 

def diaganol (board, state):
	for x in range(rows):
		for y in range(columns):
				if diag_upright(board, state, x, y) or diag_downright(board, state,x,y) :
					return true
	return false

	def full (board):
		for x in range(rows):
			for y in range(columns):
				if (board[x][y] == "empty"):
					return false
		return true

def is_terminal (board, turn):
	if (horizontal(board, turn) or vertical(board, turn) or diagonal(board, turn) or full(board)):
		return true
	else:
		return false

def possible_moves (board):
	moves = []
	x = 0
	y = 0
	while(y <= columns):
		while(x <= rows):
			if (board[x][y] != "empty"):
				moves.append(y) 
				y = y + 1
				x = 0
			else:
				x = x + 1
		y = y + 1
		x = 0
	return moves

def go_next (board, move, state):
	for x in range(rows):
		if(board[x][move] == "empty"):
			board[x][move] = state
			return board
	print "Invalid move\n"





#class Piece:
#	def __init__ (self,x_loc,y_loc,state):
#	self.r_pos = x_loc
#	self.c_pos = y_loc
#	self.state = state
