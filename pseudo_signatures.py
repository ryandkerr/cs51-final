# minimax algorithm
# node is 
def minmax(node, depth, max_player): 

#global variable to determine whose turn it is
turn = "user"

# Prompts user to select a position and recieves an int, which will
# be passed into get_move
def prompt_user:
	print("Select your move: ")
	Get int 

# Column is an int. If the column is full, return an error. Otherwise,
# place the piece of the users color in the lowest possible location
# in that column. Returns new board as an array. Sets turn to the computer.
def get_move(column):
	if column = full:
		print("Error: Column is full")
	else:
		Return board with updated piece

# Checks to see if there are 4 in a row of one color. If there are, it declares the player of that
# color then winner. Otherwise, it will either prompt the user for his move if it's the users turn,
# or it will run the minimax algorithm on the current board if it's the computer's turn.
def four_in_row(board):
	if (4 blue in a row horrizontally) || (4 blue in a row vertically) || (4 blue in a row diagonally):
		print("blue wins")
	else if:(4 red in a row horrizontally) || (4 red in a row vertically) || (4 red in a row diagonally):
		print("red wins")
	else:
		if turn = "user":
			prompt_user
		else
			minimax 