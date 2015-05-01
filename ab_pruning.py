# ab_pruning.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# Minimax algorithm using alpha-beta pruning

from board_functions import *
from evaluate import *

# minimax_ab takes a board array, depth int, player string as arguments
# minimax_ab returns the best MOVE int
# Example usage: minimax_ab(board, 5, "R") 
def minimax_ab(board, depth, state):
  
  # get array of possible moves 
  next_moves = possible_moves(board)
  best_move = next_moves[0]
  best_score = float("-inf")

  # initial alpha & beta values for alpha-beta pruning
  alpha = float("-inf")
  beta = float("inf")

  opp_state = "Y"
  if state == "Y":
    state = "Y"
    opp_state = "R"

  print state
  print opp_state

  
  # go through all of those boards
  for move in next_moves:
    
    # create new board from move
    new_board = go_next(board, move, state)

    # call min on that new board
    board_score = min_ab(new_board, depth - 1, alpha, beta, state, opp_state) - abs(move - 3)

    if board_score > best_score:
      best_score = board_score
      best_move = move

    print board_score

  return best_move


#####
# AB PRUNING MIN AND MAX PLAYER MOVES HERE
#####

# min_ab takes in a board array, depth int, alpha score and beta score
# min_ab returns the minimum SCORE for that node 
# Example usage:  min_ab(board, 3, -inf, inf)
def min_ab(board, depth, a, b, state, opp_state):
  if is_terminal(board, state):
  
    # this needs to say wether the terminal state is a draw, win, loss
    return evaluate(board, state)

  else:
    next_moves = possible_moves(board) 
    beta = b

    # if end of tree evaluate scores
    for move in next_moves:
      board_score = float("inf")

      # if furthest depth, return heuristic score of board
      if depth == 0:
        new_board = go_next(board, move, opp_state)
        board_score = evaluate(new_board, state)

      # else continue down tree as long as ab conditions met
      elif a < beta:
        new_board = go_next(board, move, opp_state)
        board_score = max_ab(new_board, depth - 1, a, beta, state, opp_state)

      if board_score < beta:
        beta = board_score

    return beta


# max_ab takes in a board array, depth int, alpha score and beta score
# max_ab returns the maximum SCORE for that node
# Example usage:  max_ab(board, 3, -inf, inf)
def max_ab(board, depth, a, b, state, opp_state):
  # check to see if game over
  if is_terminal(board, opp_state):
    # this needs to say wether the terminal state is a draw, win, loss
    return evaluate(board, state)

  else:
    next_moves = possible_moves(board) 
    alpha = a

    # if end of tree, evaluate scores
    for move in next_moves:
      board_score = float("-inf")

      # if furthest depth, return heuristic score of board
      if depth == 0:
        new_board = go_next(board, move, state)
        board_score = evaluate(new_board, state)
      
      # else continue down tree as long as ab conditions met
      elif alpha < b:
        new_board = go_next(board, move, state)
        board_score = min_ab(new_board, depth - 1, alpha, b, state, opp_state)

      if board_score > alpha:
        alpha = board_score

    return alpha