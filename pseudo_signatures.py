# MINIMAX ALGORITHM
# node is 
# depth is int for how many branches down the tree we are
# max_player is a bool that says whether or not a node is a max_player turn
#
# returns a move that results in either a:
# terminal node/move, best move for max, or best move for min
def minmax(node, depth, max_player):
    # returns the move if at a terminal state or top of tree
    if (depth = 0) or (node is terminal node):
        return heuristic value of node

    if maximizing player:
        # set best option to low value as default
        best_possibility = -1000

        # look at all children nodes, set best value to maximum
        for child in node children
            value = minimax(child, depth - 1, False)
            best_possibility = max(best_possibility, value)

        # return our best possible move
        return best_possibility
    else:
        # set best option to high value as default
        best_posibility = 1000
        for child in node children
            value = minimax(child, depth - 1, True)
            best_possibility = min(best_possibility, value)

        return best_possibility