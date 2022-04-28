import numpy as np
import oct2py 

def board_to_X(board):
    X = []
    for piece in board.white_pieces + board.black_pieces:
        X += [piece.location[0], piece.location[1], int(piece.captured)]

    return np.array(X)

def branches_to_can_p(branches):
    
