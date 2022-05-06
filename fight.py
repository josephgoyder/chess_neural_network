import engine as eg
import numpy as np
from oct2py import octave
import random


def board_to_X(board, turn):
    X = []
    for pieces in [board.white_pieces, board.black_pieces]: 
        for piece in pieces.values():
            X += [piece.location[0] / 8, piece.location[1] / 8, int(piece.captured)]

    X.append(int(turn))

    return np.array(X)


def branches_to_can_p(branches):
    return np.array([int(type(option) == dict) for option in branches])


def output_layer_to_move(branches, output_layer):
    return branches[np.argmax(output_layer)]


def fight(dataset1, dataset2):
    engine = eg.engine_setup("regular")
    octave.addpath("C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\feedforward_prop.m")
    #octave.addpath("C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\")
    #$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"

    turn = True
    while True:
        branches = engine.branches(turn)
        output_layer = octave.feedforward_prop(branches_to_can_p(branches), board_to_X(engine.board, turn), [dataset1, dataset2][int(turn)])
        engine.move(output_layer_to_move(branches, output_layer))
        engine.notebook.top_lines.clear()
        engine.search(turn, 2, branches)
        engine.illustrate(turn)

        if engine.notebook.top_lines[0][0] == 1001:
            return dataset1

        elif engine.notebook.top_lines[0][0] == -1001:
            return dataset2

        elif engine.win_lose_draw() == 0:
            return random.choice([dataset1, dataset2])

        turn = not turn 


print(fight(1, 2))