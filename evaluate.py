# evaluate.py
# Connect Four MiniMax AI
# Ryan Kerr, Milan Ravenell, Matt Tesfalul, Evan Sahdhoefner
# CS51 final project
# file that holds the evaluate function

from board_functions import *

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
        if in_row(board, "Y", 3):
            return -10
        else:
            return 5