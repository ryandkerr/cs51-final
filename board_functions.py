# board_functions.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# file holds all functions related to the board



#class GameBoard:
#   def __init__ (self):
#   self.ROWS = 7
#   self.COLUMNS = 5

COLUMNS = 7
ROWS = 6


def horizontal (board, state, length):
    for y in range(ROWS):
        in_row = 0
        for x in range(COLUMNS):
            if (board[x][y] == state):
                in_row = in_row + 1
                if (in_row == length):
                    return True
            else:
                in_row = 0
    return False

def vertical (board, state, length):
    for x in range(COLUMNS):
        in_row = 0
        for y in range(ROWS):
            if (board[x][y] == state):
                in_row = in_row + 1
                if (in_row == length):
                    return True
            else:
                in_row = 0
    return False

def diag_upright (board, state,x,y, length):
    in_row = 0
    while(y < ROWS and x < COLUMNS):
        if (board[x][y] == state):
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

def diag_downright (board, state,x,y, length):
    in_row = 0
    while(x < COLUMNS and y >= 0):
        if (board[x][y] == state):
            in_row = in_row + 1
            if(in_row == length):
                return True
            x = x + 1
            y = y - 1
        else: 
            in_row = 0
            x = x - 1
            y = y - 1
    return False 

def diagonal (board, state, length):
    for y in range(ROWS):
        for x in range(COLUMNS):
                if diag_upright(board, state, x, y, length) or diag_downright(board, state,x,y, length) :
                    return True
    return False

def full (board):
    for y in range(ROWS):
        for x in range(COLUMNS):
            if (board[x][y] == "*"):
                return False
    return True

def is_terminal (board, turn):
    if (horizontal(board, turn, 4) or vertical(board, turn, 4) or diagonal(board, turn, 4) or full(board)):
        return True
    else:
        return False

def game_won (board, turn):
    if (horizontal(board, turn, 4) or vertical(board, turn, 4) or diagonal(board, turn, 4)):
        return True
    else:
        return False

# boolean about wether there are length discs in a row
def in_row (board, turn, length):
    if (horizontal(board, turn, length) or vertical(board, turn, length) or diagonal(board, turn, length)):
        return True
    else:
        return False

def possible_moves (board):
    moves = []
    for x in range(COLUMNS):
        if (board[x][ROWS - 1] == "*"):
            moves.append(x) 
    return moves

def go_next (board, move, state):
    board1 = board 
    for y in range(ROWS):
        if(board1[move][y] == "*"):
            board1[move][y] = state
            return board1
    return board

# TESTING

board0 = [["*" for y in range(ROWS)] for x in range(COLUMNS)]


hor_board = [["*" for y in range(ROWS)] for x in range(COLUMNS)]

for y in range(ROWS):
    for x in range(COLUMNS):
        if (y%2 == 0):
            hor_board[x][y] = "R"
        else:
            hor_board[x][y] = "Y"


vert_board = [["*" for y in range(ROWS)] for x in range(COLUMNS)]
for x in range(COLUMNS):
    for y in range(ROWS):
        if (x%2 == 0):
            vert_board[x][y] = "R"
        else:
            vert_board[x][y] = "Y"


diag1_board = [["*" for y in range(ROWS)] for x in range(COLUMNS)]
diag1_board[2][2] = "R"
diag1_board[3][3] = "R"
diag1_board[4][4] = "R"
diag1_board[5][5] = "R"


diag2_board = [["*" for y in range(ROWS)] for x in range(COLUMNS)]
diag2_board[2][5] = "R"
diag2_board[3][4] = "R"
diag2_board[4][3] = "R"
diag2_board[5][2] = "R"


insert_board = [["*" for y in range(ROWS)] for x in range(COLUMNS)]
insert_board[0][0] = "R"
insert_board[1][0] = "R"
insert_board[2][0] = "R"


if (is_terminal(board0, "R") == False):
    print "success0"
if (is_terminal(hor_board, "R")):
    print "success1"
if (horizontal(vert_board, "R", 4)):
    print "failure1"
if (is_terminal(vert_board, "R")):
   print "success2"
if (vertical(hor_board, "R", 4)):
    print "failure2"
if (diagonal(vert_board, "R", 4)):
    print "failure3"
if (is_terminal(diag1_board, "R")):
    print "success3"
if (is_terminal(diag2_board, "R")):
    print "success4"
if (is_terminal(hor_board, "R")):
    print "success5"
moves1 = possible_moves(board0)
moves2 = possible_moves(hor_board)
go_board = go_next(insert_board, 3, "R")
if (is_terminal(go_board, "R")):
    print "success6"

def dummy():
    print "hey!"

#class Piece:
#   def __init__ (self,x_loc,y_loc,state):
#   self.r_pos = x_loc
#   self.c_pos = y_loc
#   self.state = state