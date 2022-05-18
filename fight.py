import engine as eg
import numpy as np
from oct2py import octave
import random
import time as tm


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
    return branches[int(output_layer) - 1]


def is_stalemate(engine, turn):
    engine.notebook.lines[0].clear()

    move_1 = engine.notebook.journey[-2]
    move_2 = engine.notebook.journey[-1]
    engine.undo()
    engine.undo()
    engine.recursive_search(turn, 2)
    engine.move(move_1)
    engine.move(move_2)

    if len(engine.notebook.lines[0][0][1]) == 0 and engine.notebook.lines[0][0][0] == 0:
        return True

    else: 
        return False


def game_turn(engine, turn, dataset1, dataset2):
    branches = engine.branches(turn)

    tic = tm.perf_counter()

    output_layer, octave_time = octave.feedforward_prop(branches_to_can_p(branches), board_to_X(engine.board, turn), [dataset1, dataset2][int(turn)], nout=2)
    print(output_layer)
    toc = tm.perf_counter()
    print(toc - tic - octave_time, octave_time)

    engine.move(output_layer_to_move(branches, output_layer))

    print("")
    engine.illustrate(True)
    print("")


def fight(dataset1, dataset2):
    engine = eg.engine_setup("regular")
    #$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"

    turn = True
    for x in range(4):
        game_turn(engine, turn, dataset1, dataset2)

        turn = not turn

    move_n = 1
    while True:
        game_turn(engine, turn, dataset1, dataset2)
        print("Move number ", move_n)
        move_n += 1
        win_lose_draw = engine.win_lose_draw()
        if win_lose_draw == 0 or is_stalemate(engine, turn) or move_n > 200:
            print("Draw")
            datasets = [dataset1, dataset2]
            random.shuffle(datasets)
            return datasets[0], datasets[1], False

        if win_lose_draw == 1000:
            print("White_wins")
            return dataset1, dataset2, True

        if win_lose_draw == -1000:
            print("Black_wins")
            return dataset2, dataset1, True

        turn = not turn 

