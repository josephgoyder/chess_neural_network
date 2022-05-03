import engine as eg
import numpy as np
from oct2py import octave
import random


def board_to_X(board):
    X = []
    for piece in board.white_pieces + board.black_pieces:
        X += [piece.location[0] / 8, piece.location[1] / 8, int(piece.captured)]

    return np.array(X)


def branches_to_can_p(branches):
    return np.array([option is dict for option in branches])


def output_layer_to_move(branches, output_layer):
    return branches[np.argmax(output_layer)]


def fight(theta1, theta2):
    engine = eg.engine_setup("regular")
    octave.addpath(".\feedforward_prop.m")

    while True:
        output_layer = octave.roundtrip(board_to_X(engine.board))
        engine.move(output_layer_to_move(output_layer))

        if abs(engine.win_lose_draw()) == 1000:
            for x in range(2):
                engine.undo()

            win_lose_draw = engine.mate_eval()

            if win_lose_draw == 1001:
                return theta1

            elif win_lose_draw == -1001:
                return theta2

            else:
                return random.choice([theta1, theta2])
