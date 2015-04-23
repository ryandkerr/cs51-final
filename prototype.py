# Prototype file for minimax algorithm

# minimax takes a board and a specified depth and outputs the best MOVE
def minimax(board, depth, max_player):
    
    # get array of possible moves 
    next_moves = board.possible_moves()
    best_move = next_moves[0]
    best_score = float("-inf")
    
    # go through all of those boards
    for move in possible_moves:
        
        # create new board from move
        new_board = board.go_next(move)

        # max player turn returns maximum of available moves
        if max_player:


        # min player choses minimum of available moves
        else


# outside of minimax call
# if we give minimax a board one move away from winning, it should output the
# winning move. Then we change the board with that move. Then we evaluate if
# that board is terminal and see if:
# is it a draw?
# is it a red player wins?
# is it a black player wins?