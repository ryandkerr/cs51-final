# evaluate.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# file that holds the evaluate function

from board_functions import *

# Checks to see if there are a series of pieces in a row of a given state for a given length.
# If there are that many in a row, it checks to see if the position before and after the series 
# are empty. If the positions before or after are empty, it checks if the position under those 
# threatening spots are empty, in which case the spot is no longer a threat. Returns a heuristic 
# proportional to the number of threatening spots the series has. The all have the same functionality
# as in board_functions.py, but with the added ability to check for the number of threatening locations.

def horizontal_threat (board, state, length):
    value = 0
    for y in range(ROWS):
        in_row = 0

        for x in range(COLUMNS):
            if (board[x][y] == state or board[x][y] == state.lower()):
                in_row = in_row + 1

                if (in_row == length):

                    # checks if there is a threatening position
                    if x < COLUMNS - 1 and board[x+1][y] == ".":

                        # checks if position below threatening position is empty
                        if y == 0 or board[x+1][y-1] != ".":
                            value = value - (length*5)

                    if x >= length and board[x-length][y] == ".":
                        if y == 0 or board[x-length][y-1] != ".":
                            value = value - (length*5)

                    return value

            else:
                in_row = 0

    return 0

def vertical_threat (board, state, length):
    value = 0
    for x in range(COLUMNS):
        in_row = 0

        for y in range(ROWS):
            if (board[x][y] == state or board[x][y] == state.lower()):
                in_row = in_row + 1

                if (in_row == length):
                    if y < ROWS - 1 and board[x][y+1] == ".":
                        value = value - (length*5)
                    return value

            else:
                in_row = 0

    return 0

def diag_upright_threat (board, state,x,y, length):
    value = 0
    in_row = 0
    while(y < ROWS and x < COLUMNS):
        if (board[x][y] == state or board[x][y] == state.lower()):
            in_row = in_row + 1

            if(in_row == length):
                if x < COLUMNS - 1 and y < ROWS - 1 and board[x+1][y+1] == "." and board[x+1][y] != ".":
                    value = value - (length*5)

                if x >= length and y >= length and board[x-length][y-length] == '.':
                    if y == length or board[x-length][y-length-1] != ".":
                        value = value - (length*5)

                return value

            x = x + 1
            y = y + 1

        else: 
            in_row = 0
            x = x + 1
            y = y + 1

    return 0

def diag_downright_threat (board, state,x,y, length):
    value = 0
    in_row = 0
    while(x < COLUMNS and y >= 0):
        if (board[x][y] == state or board[x][y] == state.lower()):
            in_row = in_row + 1

            if(in_row == length):
                if x >= length and y < ROWS - length and board[x-length][y+length] == "." and board[x-length][y+length-1] != ".":
                    value = value - (length*5)

                if x < COLUMNS - 1 and y > 0 and board[x+1][y-1] == '.':
                    if y == 1 or board[x+1][y-2] != ".":
                        value = value - (length*5)

                return value

            x = x + 1
            y = y - 1

        else: 
            in_row = 0
            x = x + 1
            y = y - 1

    return 0 

def diagonal_threat (board, state, length):
    value = 0
    for x in range(COLUMNS):
        for y in range(ROWS):
            value = value + diag_upright_threat(board, state, x, y, length) + diag_downright_threat(board, state, x, y, length)
    return value

# Returns a heuristic proportional to the number of threatening positions on the board.
def threat(board, state, length):
    return horizontal_threat(board, state, length) + vertical_threat(board, state, length) + diagonal_threat(board, state, length)


# evaluate takes a board and a player's color and outputs a SCORE based on 
# how good that board is for max payer. High score means good for max player.
def evaluate(board):

    # we need a way to see if cpu won, player won, or draw
    # right now is_term will return True if draw or if that player won
    
    # here "b" represents the computer/MAX player. If max player has won,
    # we return high score
    if game_won(board, "R"):
        return float("inf")

    elif game_won(board, "Y"):
        return float("-inf")

    elif full(board):
        return -5

    # here we define heuristics for good board
    elif threat(board, "R",3) != 0:
        return -1 * threat(board, "R",3)

    elif threat(board,"Y",3) != 0:
        return threat(board,"Y",3)

    elif threat(board, "R",2) != 0:
        return -1 * threat(board, "R",2)

    elif threat(board, "Y",2) != 0:
        return threat(board,"Y",2) 