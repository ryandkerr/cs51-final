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
            if (board[x][y] == "0"):
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
        if (board[x][ROWS - 1] == "0"):
            moves.append(x) 
    return moves

def go_next (board, move, state):
    board1 = board 
    for y in range(ROWS):
        if(board1[move][y] == "0"):
            board1[move][y] = state
            return board1
    return board

# TESTING

board0 = [["0" for y in range(ROWS)] for x in range(COLUMNS)]


hor_board = [["0" for y in range(ROWS)] for x in range(COLUMNS)]
print (hor_board)
for y in range(ROWS):
    for x in range(COLUMNS):
        if (y%2 == 0):
            hor_board[x][y] = "r"
        else:
            hor_board[x][y] = "b"
    print y


vert_board = [["0" for y in range(ROWS)] for x in range(COLUMNS)]
for x in range(COLUMNS):
    for y in range(ROWS):
        if (x%2 == 0):
            vert_board[x][y] = "r"
        else:
            vert_board[x][y] = "b"


diag1_board = [["0" for y in range(ROWS)] for x in range(COLUMNS)]
diag1_board[2][2] = "r"
diag1_board[3][3] = "r"
diag1_board[4][4] = "r"
diag1_board[5][5] = "r"


diag2_board = [["0" for y in range(ROWS)] for x in range(COLUMNS)]
diag2_board[2][5] = "r"
diag2_board[3][4] = "r"
diag2_board[4][3] = "r"
diag2_board[5][2] = "r"


insert_board = [["0" for y in range(ROWS)] for x in range(COLUMNS)]
insert_board[0][0] = "r"
insert_board[1][0] = "r"
insert_board[2][0] = "r"


if (is_terminal(board0, "r") == False):
    print "success0"
if (is_terminal(hor_board, "r")):
    print "success1"
if (horizontal(vert_board, "r", 4)):
    print "failure1"
if (is_terminal(vert_board, "r")):
   print "success2"
if (vertical(hor_board, "r", 4)):
    print "failure2"
if (diagonal(vert_board, "r", 4)):
    print "failure3"
if (is_terminal(diag1_board, "r")):
    print "success3"
if (is_terminal(diag2_board, "r")):
    print "success4"
if (is_terminal(hor_board, "r")):
    print "success5"
moves1 = possible_moves(board0)
moves2 = possible_moves(hor_board)
print (moves1)
print (moves2)
go_board = go_next(insert_board, 3, "r")
#print (go_board)
if (is_terminal(go_board, "r")):
    print "succes6"


#class Piece:
#   def __init__ (self,x_loc,y_loc,state):
#   self.r_pos = x_loc
#   self.c_pos = y_loc
#   self.state = state