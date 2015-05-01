# evaluate.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# file that holds the evaluate function

from board_functions import *

# Checks to see if there are a series of pieces in a row of a given state 
# for a given length. If there are that many in a row, it checks to see if 
# the position before and after the series are empty. If the positions before 
# or after are empty, it checks if the position under those threatening spots 
# are empty, in which case the spot is no longer a threat. Returns a heuristic 
# proportional to the number of threatening spots the series has. The all have 
# the same functionality as in board_functions.py, but with the added ability 
# to check for the number of threatening locations.

# horizontal_threat takes a board array, state string, and length int
# horizontal_threat returns an int proportional to the number threatening 
# positions if there is a series of the given length of one type horizontally
# Example usage: horizontal_threat(board, "R", 4)
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

                        # checks if position below threatening position is 
                        # empty
                        if y == 0 or board[x+1][y-1] != ".":
                            value = value - 15
                    if x >= length and board[x-length][y] == ".":
                        if y == 0 or board[x-length][y-1] != ".":
                            value = value - 15

                    return value

            else:
                in_row = 0

    return 0

# vertical_threat takes a board array, state string, and length int
# vertical_threat returns an int proportional to the number threatening 
# positions if there is a series of the given length of one type vertically
# Example usage: vertical_threat(board, "R", 4)
def vertical_threat (board, state, length):
    value = 0
    for x in range(COLUMNS):
        in_row = 0
        for y in range(ROWS):
            if y >= ROWS - 3 and in_row < 1:
                break
            if (board[x][y] == state or board[x][y] == state.lower()):
                in_row = in_row + 1
                if (in_row == length):
                    if y < ROWS - 1 and board[x][y+1] == ".":
                        value = value - 15
                    return value
            else:
                in_row = 0

    return 0

# diag_upright_threat takes a board array, state string, an x int, a y int,
# and length int
# diag_upright_threat returns an int proportional to the number threatening 
# positions if there is a series of the given length of one type starting at the
# given x and y position
# Example usage: diag_upright_threat(board, "R", 0, 0, 4)
def diag_upright_threat (board, state,x,y, length):
    value = 0
    in_row = 0
    while(y < ROWS and x < COLUMNS):
        if (board[x][y] == state or board[x][y] == state.lower()):
            in_row = in_row + 1
            if(in_row == length):
                if (x < COLUMNS - 1 and y < ROWS - 1 and 
                    board[x+1][y+1] == "." and board[x+1][y] != "."):

                    value = value - 15

                if (x >= length and y >= length and 
                    board[x-length][y-length] == "."):

                    if y == length or board[x-length][y-length-1] != ".":
                        value = value - 15
                return value
            x = x + 1
            y = y + 1

        else: 
            in_row = 0
            x = x + 1
            y = y + 1

    return 0

# diag_downright_threat takes a board array, state string, an x int, a y int,
# and length int
# diag_downright_threat returns an int proportional to the number threatening 
# positions if there is a series of the given length of one type starting at 
# the given x and y position
# Example usage: diag_downright_threat(board, "R", 0, 0, 4)
def diag_downright_threat (board, state,x,y, length):
    value = 0
    in_row = 0
    while(x < COLUMNS and y >= 0):
        if (board[x][y] == state or board[x][y] == state.lower()):
            in_row = in_row + 1
            if(in_row == length):
                if (x >= length and y < ROWS - length and 
                    board[x-length][y+length] == "." and 
                    board[x-length][y+length-1] != "."):

                    value = value - 15
                if x < COLUMNS - 1 and y > 0 and board[x+1][y-1] == ".":
                    if y == 1 or board[x+1][y-2] != ".":
                        value = value - 15
                return value
            x = x + 1
            y = y - 1

        else: 
            in_row = 0
            x = x + 1
            y = y - 1

    return 0 

# diagonal_threat takes a board array, state string, and length int
# diagonal_threat returns an int proportional to the number threatening 
# positions if there is a series of the given length of one type
# Example usage: diagonal_threat(board, "R", 4)
def diagonal_threat (board, state, length):
    value = 0
    for y in range(ROWS - 3):
        value += diag_upright_threat(board, state, 0, y, length)
    for x in range(COLUMNS - 3):
        value += diag_upright_threat(board, state, x, 0, length)
    for y in range(3, ROWS):
        value += diag_downright_threat(board, state, 0, y, length) 
    for x in range(COLUMNS - 3):
        value += diag_downright_threat(board, state, x, ROWS - 1,  length) 
    return value


# threat takes a board array, state string, and length int
# threat returns an int proportional to the number threatening 
# positions if there is a series of the given length of one type
# Example usage: threat(board, "R", 4)
def threat(board, state, length):
    return (horizontal_threat(board, state, length) + 
        vertical_threat(board, state, length) + 
        diagonal_threat(board, state, length))


# evaluate takes a board and a player's color 
# evaluate returns a  SCORE based on how good that board is for max payer.
# High score means good for max player.
def evaluate(board, state):

    # we need a way to see if cpu won, player won, or draw
    # right now is_term will return True if draw or if that player won
    
    # here "b" represents the computer/MAX player. If max player has won,
    # we return high score
    offstate = ""
    defstate =""
    if state == "R":
        offstate = state
        defstate = "Y"
    else:
        offstate = state      
        defstate = "R"

    off_threat = threat(board, offstate, 3)
    def_threat = threat(board, defstate, 3)

    if game_won(board, offstate):
        return float("inf")

    elif game_won(board, defstate):
        return float("-inf")

    # here we define heuristics for good board
    elif off_threat != 0:
        if off_threat == -30:
            return float("inf")
        else:
            return -1 * off_threat
    elif def_threat != 0:
        if def_threat == -30:
            return float("-inf")
        else: 
            return def_threat

    elif full(board):
        return 0

    else:
        return 5