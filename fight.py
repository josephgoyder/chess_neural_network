import move_undo as mv
import numpy as np
import oct2py
from pieces import King 


def board_to_X(board):
    X = []
    for piece in board.white_pieces + board.black_pieces:
        X += [piece.location[0], piece.location[1], int(piece.captured)]

    return np.array(X)


def piece_and_difference(option):
    if option["type"] == "en_passant":
        destination = option["location_3"]
    else:
        destination = option["location_2"]

    return [option["piece_key"], [option["location_1"][0] - destination[0], option["location_1"][1] - destination[1]]]


def branches_to_can_p(branches):
    return np.array([option is dict for option in branches])
