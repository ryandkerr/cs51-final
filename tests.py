# tests.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# Test file for minimax algorithm


from board_functions import *
from evaluate import *


# TESTING board_functions

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

# Creates a board into which we will call go_next and insert a piece 
# of the same state
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

#------------------------------------------------------------------
# Threat Tests 

# Creates a board with 3 in a row diagonally upright
verts_board = [["." for y in range(ROWS)] for x in range(COLUMNS)]
verts_board[3][0] = "R"
verts_board[3][1] = "R"
verts_board[3][2] = "R"

if (vertical_threat(verts_board, "R", 3) != -15):
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


if (horizontal_threat(horz_board, "R", 3) != -15):
    print "Failure for horizontal threat"
if (horizontal_threat(horz_board2, "R", 3) != -30):
    print "Failure for horizontal1 index_outbounds"
if (horizontal_threat(horz_board3, "R", 3) != -15):
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


if (diag_downright_threat(diag_board1, "R", 0, 3, 3) != -15):
    print "Failure diagnol downright"
if (diag_upright_threat(diag_board2, "R", 0, 0, 3) != -30):
    print "Failure diagnol upright" 
if (diag_upright_threat(diag_board3, "R", 0, 0, 3) != 0):
    print "Failure diagnol upright" 
if ((diagonal_threat (diag_board1, "R", 3) != -15) and 
    (diagonal_threat(diag_board2, "R", 3) != -30)):
    print "Failure diagnol function"

