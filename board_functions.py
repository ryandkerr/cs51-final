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

# Returns true if there are a series of the specified state of the given length horizontally
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

# Returns true if there are a series of the specified state of the given length vertically
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

# Returns true if there are a series of the specified state of the given length diagonally in the upright direction at a given point
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
# Returns true if there are a series of the specified state of the given length diagonally in the downright direction at a given point
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

# Iterates the diagonal upright and diagonal downright over the possible positions where there could be a 4 in a row diagonally 
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

# Returns true if a player has won or if the board is full
def is_terminal (board, turn):
    if (horizontal(board, turn, 4) or vertical(board, turn, 4) or diagonal(board, turn, 4) or full(board)):
        return True
    else:
        return False

# Returns true if a player has won
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

# Returns a list of ints that represent the columns where we could possibly place a piece
def possible_moves (board):
    moves = []
    for x in range(COLUMNS):
        if (board[x][ROWS - 1] == "."):
            moves.append(x) 
    return moves

# Given a board, an int, and a piece color, it will return a new board with that piece inserted into the lowest possible location
# at the column that is represented by the int
def go_next (board, move, state):
    board1 = copy_board(board) 
    for y in range(ROWS):
        if(board1[move][y] == "."):
            board1[move][y] = state
            return board1




