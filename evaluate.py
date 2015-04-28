# evaluate.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# file that holds the evaluate function

from board_functions import *

def horizontal_threat (board, state, length):
    value = 0
    for y in range(ROWS):
        in_row = 0
        for x in range(COLUMNS):
            if (board[x][y] == state):
                in_row = in_row + 1
                if (in_row == length):
                    if (x > 0):
                        if board[x-1][y] == ".":
                            value = value - 1
                    if (x < COLUMNS - length):
                        if board[x+length][y] == '.':
                            value = value - 1
                    return value
            else:
                in_row = 0
    return 0

def vertical_threat (board, state, length):
    value = 0
    for x in range(COLUMNS):
        in_row = 0
        for y in range(ROWS):
            if (board[x][y] == state):
                in_row = in_row + 1
                if (in_row == length):
                    if (y > 0):
                        if board[x][y-1] == ".":
                            value = value - 1
                    if (y < ROWS - length):
                        if board[x][y+length] == '.':
                            value = value - 1
                    return value
            else:
                in_row = 0
    return 0

def diag_upright_threat (board, state,x,y, length):
    value = 0
    in_row = 0
    while(y < ROWS and x < COLUMNS):
        if (board[x][y] == state):
            in_row = in_row + 1
            if(in_row == length):
                if (x > 0 and y > 0):
                    if board[x-1][y-1] == ".":
                        value = value - 1
                if (x < COLUMNS - length and y < ROWS - length):
                    if board[x+length][y+length] == '.':
                        value = value - 1
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
        if (board[x][y] == state):
            in_row = in_row + 1
            if(in_row == length):
                if (x > 0 and y < ROWS):
                    if board[x-1[y+1] == ".":
                        value = value - 1
                if (x < COLUMNS - length and y >= length):
                    if board[x+length][y-length] == '.':
                        value = value - 1
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

def threat(board, state, length):
    value = 0
        value = value + (horizontal_threat(board, state, length) + vertical_threat(board, state, length) + diagonal_threat(board, state, length)
    return value


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
        return 0
    else:
        # here we define heuristics for good board
        return threat(board,"Y",3)

        # if in_row(board, "Y", 3):
        #     return -10
        # else:
        #     return 5