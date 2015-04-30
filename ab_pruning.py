# prototype.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# Prototype file for minimax algorithm

from board_functions import *
from evaluate import *

# minimax takes a board and a specified depth and outputs the best MOVE
def minimax_ab(board, depth):
  
  # get array of possible moves 
  next_moves = possible_moves(board)
  best_move = next_moves[0]
  best_score = float("-inf")

  alpha = float("-inf")
  beta = float("inf")

  
  # go through all of those boards
  for move in next_moves:
    
    # create new board from move
    new_board = go_next(board, move, "R")

    # call min on that new board
    board_score = min_ab(new_board, depth - 1, alpha, beta) + (move % 4)

    if board_score > best_score:
      best_score = board_score
      best_move = move

  return best_move


# min player is given a board and choses the lowest option, returns a SCORE
def min_player(board, depth):
  if is_terminal(board, "R"):
  
    # this needs to say wether the terminal state is a draw, win, loss
    return evaluate(board)

  else:
    next_moves = possible_moves(board) 
    min_score = float("inf")

    # if end of tree evaluate scores
    for move in next_moves:
      new_board = go_next(board, move, "Y")

      board_score = 0

      if depth == 0:
        board_score = evaluate(new_board)
      else:
        board_score = max_player(new_board, depth - 1)

      if board_score < min_score:
        min_score = board_score

    return min_score


# max player picks max move and outputs SCORE
def max_player(board, depth):
  if is_terminal(board, "Y"):
  
    # this needs to say wether the terminal state is a draw, win, loss
    return evaluate(board)

  else:
    next_moves = possible_moves(board) 
    max_score = float("-inf")

    # if end of tree, evaluate scores
    for move in next_moves:
      new_board = go_next(board, move, "R")

      board_score = 0

      if depth == 0:
        board_score = evaluate(new_board)
      else:
        board_score = min_player(new_board, depth - 1)

      if board_score > max_score:
        max_score = board_score

    return max_score


# outside of minimax call
# if we give minimax a board one move away from winning, it should output the
# winning move. Then we change the board with that move. Then we evaluate if
# that board is terminal and see if:
# is it a draw?
# is it a red player wins?
# is it a black player wins?

# AB PRUNING MIN AND MAX PLAYER MOVES HERE
# returns a score
# min_ab(board, 3, -inf, inf) returns a score
def min_ab(board, depth, a, b):
  if is_terminal(board, "R"):
  
    # this needs to say wether the terminal state is a draw, win, loss
    return evaluate(board)

  else:
    next_moves = possible_moves(board) 
    beta = b

    # if end of tree evaluate scores
    for move in next_moves:
      board_score = float("inf")

      if depth == 0:
        new_board = go_next(board, move, "Y")
        board_score = evaluate(new_board)

      elif a < beta:
        new_board = go_next(board, move, "Y")
        board_score = max_ab(new_board, depth - 1, a, beta)

      if board_score < beta:
        beta = board_score

    return beta



def max_ab(board, depth, a, b):
  if is_terminal(board, "Y"):
  
    # this needs to say wether the terminal state is a draw, win, loss
    return evaluate(board)

  else:
    next_moves = possible_moves(board) 
    alpha = a

    # if end of tree, evaluate scores
    for move in next_moves:
      board_score = float("-inf")

      if depth == 0:
        new_board = go_next(board, move, "R")
        board_score = evaluate(new_board)
      elif alpha < b:
        new_board = go_next(board, move, "R")
        board_score = min_ab(new_board, depth - 1, alpha, b)

      if board_score > alpha:
        alpha = board_score

    return alpha