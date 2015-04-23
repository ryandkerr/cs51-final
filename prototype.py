# Prototype file for minimax algorithm

# minimax takes a board and a specified depth and outputs the best MOVE
def minimax(board, depth):
    
    # get array of possible moves 
    next_moves = board.possible_moves()
    best_move = next_moves[0]
    best_score = float("-inf")
    
    # go through all of those boards
    for move in next_moves:
        
        # create new board from move
        new_board = board.go_next(move)

        # call min on that new board
        board_score = min_player(new_board, depth - 1)

        if board_score > best_score:
            best_score = board_score
            best_move = move

    return best_move

def min_player(board, depth):
    if board.is_terminal():
    
        # this needs to say wether the terminal state is a draw, win, loss
        return evaluate(board)

    else next_moves = board.possible_moves() 
    worst_move = next_moves[0]
    worst score = float("inf")

    # if end of tree evaluate scores
    if depth == 0:
        
    # else call max on the board possibility
    else 


# outside of minimax call
# if we give minimax a board one move away from winning, it should output the
# winning move. Then we change the board with that move. Then we evaluate if
# that board is terminal and see if:
# is it a draw?
# is it a red player wins?
# is it a black player wins?