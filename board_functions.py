# board_functions.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# file holds all functions related to the board



#class GameBoard:
#   def __init__ (self):
#   self.ROWS = 7
#   self.COLUMNS = 5

# globals
COLUMNS = 7
ROWS = 6

# copies board without changing original board
def copy_board(board):
    copy = [["." for y in range(ROWS)] for x in range(COLUMNS)]
    for x in range(COLUMNS):
        for y in range(ROWS):
            copy[x][y] = board[x][y]
    return copy

# Given a board, string signifying the turn, and a length(int), returns true 
# if there are a series of the specified state of the given length horizontally
def horizontal (board, state, length):
    for y in range(ROWS):
        in_row = 0
        for x in range(COLUMNS):
            if (board[x][y] == state or board[x][y] == state.lower()):
                in_row = in_row + 1
                if (in_row == length):
                    return True
            else:
                in_row = 0
    return False

# Given a board, string signifying the turn, and a length(int), returns true 
# if there are a series of the specified state of the given length vertically.
def vertical (board, state, length):
    for x in range(COLUMNS):
        in_row = 0
        for y in range(ROWS):
            if (board[x][y] == state or board[x][y] == state.lower()):
                in_row = in_row + 1
                if (in_row == length):
                    return True
            elif (board[x][y] == "."):
                in_row = 0
                break
            else:
                in_row = 0
    return False

# Given a board, string signifying the turn, an x and y position, and a 
# length(int), Returns true if there are a series of the specified state 
# of the given length diagonally in the downright direction at a given point.
def diag_upright (board, state,x,y, length):
    in_row = 0
    while(y < ROWS and x < COLUMNS):
        if (board[x][y] == state or board[x][y] == state.lower()):
            in_row = in_row + 1
            if(in_row == length):
                return True
            x = x + 1
            y = y + 1
        else: 
            in_row = 0
            x = x + 1
            y = y + 1
    return False

# Given a board, string signifying the turn, an x and y position, and a 
# length(int), Returns true if there are a series of the specified state 
# of the given length diagonally in the downright direction at a given point.
def diag_downright (board, state,x,y, length):
    in_row = 0
    while(x < COLUMNS and y >= 0):
        if (board[x][y] == state or board[x][y] == state.lower()):
            in_row = in_row + 1
            if(in_row == length):
                return True
            x = x + 1
            y = y - 1
        else: 
            in_row = 0
            x = x + 1
            y = y - 1
    return False 

# Given a board, a string signifying the turn, and a length(int), iterates 
# the diagonal upright and diagonal downright over the possible positions 
# where there could be a 4 in a row diagonally.
def diagonal (board, state, length):
    for y in range(ROWS - 3):
        if diag_upright(board, state, 0, y, length) :
            return True
    for x in range(COLUMNS - 3):
        if diag_upright(board, state, x, 0, length) :
            return True
    for y in range(3, ROWS):
        if diag_downright(board, state, 0, y, length) :
            return True
    for x in range(COLUMNS - 3):
         if diag_downright(board, state, x, ROWS - 1,  length) :
            return True
    return False

# Returns true if the board is full
def full (board):
    for y in range(ROWS):
        for x in range(COLUMNS):
            if (board[x][y] == "."):
                return False
    return True

# Given a board and a string signyfing the turn, returns true if that player 
# has won or if the board is full.
def is_terminal (board, turn):
    return (horizontal(board, turn, 4) or vertical(board, turn, 4) or 
        diagonal(board, turn, 4) or full(board))

# Given a board and a string signyfing the turn, returns true if that player 
# has won.
def game_won (board, turn):
    return (horizontal(board, turn, 4) or vertical(board, turn, 4) or 
        diagonal(board, turn, 4))
       

# Given a board, a string signifying the turn, and a length(int), returns true
# if there is a series of the given player's piece of the given length.
def in_row (board, turn, length):
    return (horizontal(board, turn, length) or vertical(board, turn, length) 
        or diagonal(board, turn, length))

# Given a board, returns a list of ints that represent the columns where we 
# could possibly place a piece
def possible_moves (board):
    moves = []
    for x in range(COLUMNS):
        if (board[x][ROWS - 1] == "."):
            moves.append(x) 
    return moves

# Given a board, an int, and a piece color, it will return a new board with 
# that piece inserted into the lowest possible location at the column that is
# represented by the int
def go_next (board, move, state):
    board1 = copy_board(board) 
    for y in range(ROWS):
        if(board1[move][y] == "."):
            board1[move][y] = state
            return board1

# TESTING

# Creates an empty board
board0 = [["." for y in range(ROWS)] for x in range(COLUMNS)]

# Creates a board with 4 in a row horizontally
hor_board = [["." for y in range(ROWS)] for x in range(COLUMNS)]

for y in range(ROWS):
    for x in range(COLUMNS):
        if (y%2 == 0):
            hor_board[x][y] = "R"
        else:
            hor_board[x][y] = "Y"

# Creates a board with 4 in a row vertically
vert_board = [["." for y in range(ROWS)] for x in range(COLUMNS)]
for x in range(COLUMNS):
    for y in range(ROWS):
        if (x%2 == 0):
            vert_board[x][y] = "R"
        else:
            vert_board[x][y] = "Y"


# Creates a board with 4 in a row diagonally upright
diag1_board = [["." for y in range(ROWS)] for x in range(COLUMNS)]
diag1_board[2][2] = "R"
diag1_board[3][3] = "R"
diag1_board[4][4] = "R"
diag1_board[5][5] = "R"

# Creates a board with 4 in a row diagonally downright
diag2_board = [["." for y in range(ROWS)] for x in range(COLUMNS)]
diag2_board[0][4] = "R"
diag2_board[1][3] = "R"
diag2_board[2][2] = "R"
diag2_board[3][1] = "R"

# Creates a board into which we will call go_next and insert a piece of the 
# same state
insert_board = [["." for y in range(ROWS)] for x in range(COLUMNS)]
insert_board[0][0] = "R"
insert_board[1][0] = "R"
insert_board[2][0] = "R"


if (is_terminal(board0, "R") != False):
   print "failure0"
if (is_terminal(hor_board, "R") == False):
    print "failure0.5"
if (horizontal(vert_board, "R", 4)):
    print "failure1"
if (is_terminal(vert_board, "R") == False):
   print "failure1.5"
if (vertical(hor_board, "R", 4)):
    print "failure2"
if (diagonal(vert_board, "R", 4)):
    print "failure3"
if (is_terminal(diag1_board, "R") == False):
    print "failure3.5"
if (is_terminal(diag2_board, "R") == False):
    print "failure4"
if (is_terminal(hor_board, "R") == False):
   print "failure5"
moves1 = possible_moves(board0)
moves2 = possible_moves(hor_board)
go_board = go_next(insert_board, 3, "R")
if (is_terminal(go_board, "R") == False):
   print "failure6"
    

# testing go_next to see if it changes original
empty = [["." for y in range(ROWS)] for x in range(COLUMNS)]
moved = go_next(empty, 1, "R")




