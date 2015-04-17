# MINIMAX ALGORITHM
# node is 
# depth is int for how many branches down the tree we are
# max_player is a bool that says whether or not a node is a max_player turn
#
# returns a move that results in either a:
# terminal node/move, best move for max, or best move for min
def minmax(node, depth, max_player):
    # returns the move if at a terminal state or top of tree
    if (depth = 0) or (node is terminal node):
        return heuristic value of node

    if max_player:
        # set best option to low value as default
        best_possibility = -1000

        # look at all children nodes, set best value to maximum
        for child in node children
            value = minimax(child, depth - 1, False)
            best_possibility = max(best_possibility, value)

        # return our best possible move
        return best_possibility
    else:
        # set best option to high value as default
        best_posibility = 1000
        for child in node children
            value = minimax(child, depth - 1, True)
            best_possibility = min(best_possibility, value)

        return best_possibility

# ALPHABETA PRUNING ALGORITHM
# node is a node on the minimax tree
# depth is an int for how many brnaches down the tree we are
# max_player is a bool saying wether or not node is a max_player turn
# a is a node that represents max's best choice from a given node
# b is a node that represents min's best choice from a given node
#
# returns heuristic value node, alpha node from max, or beta node from min
def abprune(node, depth, a, b, max_player):
    if (depth = 0) or (node is terminal node):
        return heuristic value of node

    # returns the best choice for max player
    if max_player:
        for child in node children
            a = max(a, abprune(child, depth - 1, a, b, False))
            if a >= b:
                finish pruning

        return a
    # returns best choice for min player
    else:
        for child in node children
            b = min(b, abprune(child, depth - 1, a, b, True))
            if b <= a:
                finish pruning

        return b



#global variable to determine whose turn it is
turn = "user"

def next_move:
	if turn = "user":
		user_move
	else:
		minimax


# Prompts user to select a position and recieves an int, which will
# be passed into get_move
def prompt_user:
	print("Select your move: ")
	Get int 

# Column is an int. If the column is full, return an error. Otherwise,
# place the piece of the users color in the lowest possible location
# in that column. Returns new board as an array. Sets turn to the computer.
def user_move(column):
	if column = full:
		print("Error: Column is full")
	else:
		Return board with updated piece
	global turn = "computer"
	next_move


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

# Prints the board as an ASCII representation
def print_board (board):
	for x in range (0,columns):
		for y in range (0,rows):
			if board(x,y) = red:
				print("r")
			else if board(x,y) = blue:
				print("b")
			else:
				print("o")



