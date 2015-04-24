#class GameBoard:
#	def __init__ (self):
#	self.rows = 7
#	self.columns = 5

columns = 7
rows = 6

def horizontal (board, state):
	for y in range(columns):
		in_row = 0
		for x in range(rows):
			if (board[x][y] == state):
				in_row = in_row + 1
				if (in_row == 4):
					return True
			else:
				in_row = 0
	return False

def vertical (board, state):
	for x in range(rows):
		in_row = 0
		for y in range(columns):
			if (board[x][y] == state):
				in_row = in_row + 1
				if (in_row == 4):
					return True
			else:
				in_row = 0
	return False

def diag_upright (board, state,x,y):
	in_row = 0
	while(x <= rows and y <= columns):
		if (board[x][y] == state):
			in_rows = in_rows + 1
			if(in_row == 4):
				return True
			x = x + 1
			y = y + 1
		else: 
			in_row = 0
			x = x + 1
			y = y + 1
	return False

def diag_downright (board, state,x,y):
	in_row = 0
	while(x >= 0 and y >= 0):
		if (board[x][y] == state):
			in_rows = in_rows + 1
			if(in_row == 4):
				return True
			x = x - 1
			y = y - 1
		else: 
			in_row = 0
			x = x - 1
			y = y - 1
	return False 

def diaganol (board, state):
	for x in range(rows):
		for y in range(columns):
				if diag_upright(board, state, x, y) or diag_downright(board, state,x,y) :
					return True
	return False

def full (board):
	for x in range(rows):
		for y in range(columns):
			if (board[x][y] == "0"):
				return False
	return True

def is_terminal (board, turn):
	if (horizontal(board, turn) or vertical(board, turn) or diagonal(board, turn) or full(board)):
		return True
	else:
		return False

def possible_moves (board):
	moves = []
	x = 0
	y = 0
	while(y <= columns):
		while(x <= rows):
			if (board[x][y] != "0"):
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
		if(board[x][move] == "0"):
			board[x][move] = state
			return board
	print "Invalid move\n"

# TESTING

board0 = [["0" for y in range(columns)] for x in range(rows)]


board1 = board0
for x in range(rows):
	for y in range(columns):
		if (x%2 == 0):
			board1[x][y] = "r"
		else:
			board1[x][y] = "b"



board2 = board0
for y in range(columns):
	for x in range(rows):
		if (y%2 == 0):
			board2[x][y] = "r"
		else:
			board2[x][y] = "b"



board3 = board1
board3[2][2] = "r"
board3[3][3] = "r"
board3[4][4] = "r"
board3[5][5] = "r"



board4 = board1
board4[2][5] = "r"
board4[3][4] = "r"
board4[4][3] = "r"
board4[5][2] = "r"


board5 = board0
board5[1][1] = "r"
board5[1][2] = "r"
board5[1][3] = "r"




def test:
	if (is_terminal(board0, "r") == False):
		print "success0"
	if (horizontal(board1, "r") == True):
		print "success1"
	if (vertical(board2, "r") == True):
		print "success2"
	if (diag_upright(board3, "r") == True):
		print "success3"
	if (diag_downright(board4, "r") == True):
		print "success4"
	if (full(board1) == True):
		print "success5"
	print possible_moves(board0)
	print possible_moves(board1)
	if horizontal(go_next(board5,4, "r"))):
		print "succes6"


















#class Piece:
#	def __init__ (self,x_loc,y_loc,state):
#	self.r_pos = x_loc
#	self.c_pos = y_loc
#	self.state = state
