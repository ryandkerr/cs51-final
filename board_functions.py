# board_functions.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# file holds all functions related to the board

# globals
COLUMNS = 7
ROWS = 6

# copy_board takes in a board array
# copy_board returns a copied board without changing original
# Exmaple usage: copy_board(board)
def copy_board(board):
  copy = [["." for y in range(ROWS)] for x in range(COLUMNS)]
  for x in range(COLUMNS):
      for y in range(ROWS):
          copy[x][y] = board[x][y]
  return copy

# horizontal takes a board array, state string, and length int
# horizontal returns true if there is a series of the given length of one type
# horizontally
# Example usage: horizontal(board, "R", 4)
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

# vertical takes a board array, state string, and length int
# vertical returns true if there is a series of the given length of one type
# vertically 
# Example usage: vertical(board, "R", 4)
def vertical(board, state, length):
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

# diag_upright takes a board array, state string, an x int, a y int, 
# and length int
# diag_upright returns true if there is a series of the given length of one type
# starting at the x and y position
# Example usage: diag_upright(board, "R", 0, 0, 4)
def diag_upright(board, state,x,y, length):
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

# diag_downright takes a board array, state string, an x int, a y int, 
# and length int
# diag_downright returns true if there is a series of the given length of one type
# starting at the x and y position
# Example usage: diag_downright(board, "R", 0, 0, 4)
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

# diagonal takes a board array, state string, and length int
# diagonal returns true if there is a series of the given length of one type
# diagonally
# Example usage: diag_upright(board, "R", 0, 0, 4)
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

# full takes a board array
# full returns true if the board is full
# Example usage: full(board)
def full (board):
  for y in range(ROWS):
    for x in range(COLUMNS):
      if (board[x][y] == "."):
        return False
  return True

# is_terminal takes a board array, and a state string
# is_terminal returns true if there is 4 in a row of one player or the board is 
# full
# Example usage: is_terminal(board, "R")
def is_terminal (board, turn):
  return (horizontal(board, turn, 4) or vertical(board, turn, 4) or 
    diagonal(board, turn, 4) or full(board))

# game_won takes a board array, and a state string
# game_won returns true if there is 4 in a row of one player 
# Example usage: game_won(board, "R")
def game_won (board, turn):
  return (horizontal(board, turn, 4) or vertical(board, turn, 4) or 
    diagonal(board, turn, 4))
       

# in_row takes a board array, state string, and a length int
# in_row returns true if there is 4a series of the given length of one
# player
# Example usage: in_row(board, "R", 3)
def in_row (board, turn, length):
    return (horizontal(board, turn, length) or vertical(board, turn, length) 
        or diagonal(board, turn, length))

# possible_moves takes a board array
# possible_moves returns an int list of the possible columns where a piece could
# be placed
# Example usage: possible_moves(board, "R")
def possible_moves (board):
    moves = []
    for x in range(COLUMNS):
        if (board[x][ROWS - 1] == "."):
            moves.append(x) 
    return moves

# go_next takes a board array, a move int, and a state string
# go_next returns an updated board with a piece in the lowest possible
# spot in the column of the given int
# Example usage: go_next(board, 4, "R")
def go_next (board, move, state):
    board1 = copy_board(board) 
    for y in range(ROWS):
        if(board1[move][y] == "."):
            board1[move][y] = state
            return board1





