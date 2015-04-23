# board_functions.py
# Connect Four MiniMax AI
# CS 51 Final Project
# Evan Sandhoefner, Ryan Kerr, Milan Ravenell, Matthew Tesfalul
# classes and functions about our board data structure

class GameBoard:
    def __init__ (self, board):
    self.rows = 7
    self.columns = 5

    self.board = board

    def horizontal (state):
        for y in range(columns):
            in_row = 0
            for x in range(rows):
                if (Board[x][y]).state = state:
                    in_row = in_row + 1
                    if (in_row = 4):
                        return true
                else:
                    in_row = 0
        return false

    def vertical (state):
        for x in range(rows):
            in_row = 0
            for y in range(columns):
                if (Board[x][y]).state = state:
                    in_row = in_row + 1
                    if (in_row = 4):
                        return true
                else:
                    in_row = 0
        return false

    def diag_upright (state,x,y):
        in_row = 0
        while(x <= rows && y <= columns):
            if ((Board[x][y]).state = state):
                in_rows = in_rows + 1
                if(in_row = 4):
                    return true
                x = x + 1
                y = y + 1
            else: 
                in_row = 0
                x = x + 1
                y = y + 1
        return false

    def diag_downright (state,x,y):
        in_row = 0
        while(x >= 0 && y >= 0):
            if ((Board[x][y]).state = state):
                in_rows = in_rows + 1
                if(in_row = 4):
                    return true
                x = x - 1
                y = y - 1
            else: 
                in_row = 0
                x = x - 1
                y = y - 1
        return false 

    def diaganol (state):
        for x in range(rows):
            for y in range(columns):
                    if diag_upright(state, x, y) or diag_downright(state,x,y) :
                        return true
        return false

        def full:
            for x in range(rows):
                for y in range(columns):
                    if ((Board[x][y]).state = "empty"):
                        return false
            return true

    def is_terminal board(turn):
        if (horizontal(turn) or vertical(turn) or diagonal(turn) or full):
            return true
        else:
            return false

    def possible_moves 

    def go_next  



class Piece:
    def __init__ (self,x_loc,y_loc,state):
    self.r_pos = x_loc
    self.c_pos = y_loc
    self.state = state

slot = Piece(0,0,"empty")
Board = [[slot for x in range(rows)] for y in range(columns)]

for x in range(rows):
    for y in range(columns):
        slot = Piece(x,y,"empty")
        Matrix[x][y] = spot
