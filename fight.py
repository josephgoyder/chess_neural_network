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
    octave.addpath("\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin")

    turn = True
    while True:
        branches = engine.branches()
        output_layer = octave.roundtrip(branches_to_can_p(branches), board_to_X(engine.board), 1)
        engine.move(output_layer_to_move(branches, output_layer))
        engine.notebook.top_lines.clear()
        engine.search(turn, 2, branches)

        if engine.notebook.top_lines[0][0] == 1001:
            return theta1

        elif engine.notebook.top_lines[0][0] == -1001:
            return theta2

        elif engine.win_lose_draw() == 0:
            return random.choice([theta1, theta2])

        turn = not turn 
