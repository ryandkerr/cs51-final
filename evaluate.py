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

# Given a board, a string signifying the turn, and a length, 
def horizontal_threat (board, state, length):
    value = 0
    for y in range(ROWS):
        in_row = 0

        for x in range(COLUMNS):
            if x >= COLUMNS - 3 and in_row < 1:
                break

            if (board[x][y] == state or board[x][y] == state.lower()):
                in_row = in_row + 1

                if (in_row == length):
                    # checks if there is a threatening position
                    if x < COLUMNS - 1 and board[x+1][y] == ".":

                        # checks if position below threatening position is empty
                        if y == 0 or board[x+1][y-1] != ".":
                            value = value - (length*length*5)

                    if x >= length and board[x-length][y] == ".":
                        if y == 0 or board[x-length][y-1] != ".":
                            value = value - (length*length*5)
                    return value

            else:
                in_row = 0

    return 0

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
                        value = value - (length*length*5)
                    return value

            else:
                in_row = 0

    return 0

def diag_upright_threat (board, state,x,y, length):
    value = 0
    in_row = 0
    while(y < ROWS and x < COLUMNS):
        if (x >= COLUMNS - 3 or y >= ROWS - 3) and in_row < 1:
            break

        if (board[x][y] == state or board[x][y] == state.lower()):
            in_row = in_row + 1
            if(in_row == length):
                if x < COLUMNS - 1 and y < ROWS - 1 and board[x+1][y+1] == "." and board[x+1][y] != ".":
                    value = value - (length*length*5)
                if x >= length and y >= length and board[x-length][y-length] == '.':
                    if y == length or board[x-length][y-length-1] != ".":
                        value = value - (length*length*5)
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
        if (x >= COLUMNS - 3 or y < 3) and in_row < 1:
            break

        if (board[x][y] == state or board[x][y] == state.lower()):
            in_row = in_row + 1
            if(in_row == length):
                if x >= length and y < ROWS - length and board[x-length][y+length] == "." and board[x-length][y+length-1] != ".":
                    value = value - (length*length*5)
                if x < COLUMNS - 1 and y > 0 and board[x+1][y-1] == '.':
                    if y == 1 or board[x+1][y-2] != ".":
                        value = value - (length*length*5)
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
    for y in range(ROWS - 3):
        value += diag_upright_threat(board, state, 0, y, length)
    for x in range(COLUMNS - 3):
        value += diag_upright_threat(board, state, x, 0, length)
    for y in range(3, ROWS):
        value += diag_downright_threat(board, state, 0, y, length) 
    for x in range(COLUMNS - 3):
        value += diag_downright_threat(board, state, x, ROWS - 1,  length) 
    return value

# Threat Tests 

# Creates a board with 3 in a row diagonally upright
verts_board = [["." for y in range(ROWS)] for x in range(COLUMNS)]
verts_board[3][0] = "R"
verts_board[3][1] = "R"
verts_board[3][2] = "R"

if (vertical_threat(verts_board, "R", 3) != -45):
    print "Failure vertictal threat"

# threat of -45 horizontally
horz_board = [["." for y in range(ROWS)] for x in range(COLUMNS)]
horz_board[0][2] = "R"
horz_board[1][2] = "R"
horz_board[2][2] = "R"
# placeholder so that test knows column is filled up 
horz_board[3][1] = "Y"

#second horizontal index outbounds test with no placeholder
horz_board2 = [["." for y in range(ROWS)] for x in range(COLUMNS)]
horz_board2[1][0] = "R"
horz_board2[2][0] = "R"
horz_board2[3][0] = "R"

#second horizontal index outbounds test with no placeholder
horz_board3 = [["." for y in range(ROWS)] for x in range(COLUMNS)]
horz_board3[4][0] = "R"
horz_board3[5][0] = "R"
horz_board3[6][0] = "R"

if (horizontal_threat(horz_board, "R", 3) != -45):
    print "Failure for horizontal threat"
if (horizontal_threat(horz_board2, "R", 3) != -90):
    print "Failure for horizontal1 index_outbounds"
if (horizontal_threat(horz_board3, "R", 3) != -45):
    print "Failure for horizontal2 index_outbounds"




# Creates a board with 3 in a row diagonally downright without placeholder
diag_board1 = [["." for y in range(ROWS)] for x in range(COLUMNS)]
diag_board1[0][3] = "R"
diag_board1[1][2] = "R"
diag_board1[2][1] = "R"

# no need for placeholder to fill column 

# Creates a board with 3 in a row diagnally upright
diag_board2 = [["." for y in range(ROWS)] for x in range(COLUMNS)]
diag_board2[1][1] = "R"
diag_board2[2][2] = "R"
diag_board2[3][3] = "R"

#placeholder to signal column filled
diag_board2[4][3] = "Y"

# Creates a board with 3 in a row diagnally upright
diag_board3 = [["." for y in range(ROWS)] for x in range(COLUMNS)]
diag_board3[0][1] = "R"
diag_board3[1][2] = "R"
diag_board3[2][3] = "R"


if (diag_downright_threat(diag_board1, "R", 0, 3, 3) != -45):
    print "Failure diagonal downright"
if (diag_upright_threat(diag_board2, "R", 0, 0, 3) != -90):
    print "Failure diagonal upright" 
if (diag_upright_threat(diag_board3, "R", 0, 0, 3) != 0):
    print "Failure diagonal upright" 
if (diagonal_threat (diag_board1, "R", 3) != -45) and (diagonal_threat(diag_board2, "R", 3) != 90):
    print "Failure diagonal function"

# non diag down right threat 
two_board = [["." for y in range(ROWS)] for x in range(COLUMNS)]
two_board[0][2] = "R"
two_board[1][1] = "R"

# double diag up right threat of -90 
two_board1 = [["." for y in range(ROWS)] for x in range(COLUMNS)]
two_board1[4][3] = "R"
two_board1[5][4] = "R"
#placeholders to show columns are filled
two_board1[6][4] = "Y"
two_board1[3][1] = "Y"

if (diagonal_threat(two_board, "R", 2) != 0):
    print "Failure length 2 diagonal downward"

if (diagonal_threat(two_board1, "R", 2) != -40):
    print "Failure length 2 diagonal upward"

# Returns a heuristic proportional to the number of threatening positions on the board.
def threat(board, state, length):
    return horizontal_threat(board, state, length) + vertical_threat(board, state, length) + diagonal_threat(board, state, length)


# evaluate takes a board and a player's color and outputs a SCORE based on 
# how good that board is for max payer. High score means good for max player.
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
        offstate == state      
        defstate == "R"

    off_threat = threat(board, offstate, 3)
    def_threat = threat(board, defstate, 3)

    if game_won(board, offstate):
        return float("inf")

    elif game_won(board, defstate):
        return float("-inf")

    elif full(board):
        return 0

    # here we define heuristics for good board
    elif off_threat != 0:
        return -1 * off_threat

    elif def_threat != 0:
        return def_threat

    else:
        return 5
