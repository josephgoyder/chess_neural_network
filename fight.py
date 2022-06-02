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

    X.append(int(turn) * 2 - 1)

    return np.array(X)


def branches_to_can_p(branches):
    return np.array([int(type(option) == dict) for option in branches])


def output_layer_to_move(branches, output_layer):
    return branches[int(output_layer) - 1]


def engine_mate_eval(engine, turn):
    engine.notebook.lines[0].clear()

    engine.recursive_search(turn, 2)
    

    if len(engine.notebook.lines[0][0][1]) == 0:
        return engine.notebook.lines[0][0][0]


def is_stalemate(engine, turn, move_n):
    if move_n < 4:
        return False

    move_1 = engine.notebook.journey[-2]
    move_2 = engine.notebook.journey[-1]
    engine.undo()
    engine.undo()
    win_lose_draw = engine_mate_eval(engine, turn)
    engine.move(move_1)
    engine.move(move_2)

    if win_lose_draw == 0:
        return True
    
    return False


def nn_move(engine, turn, dataset):
    branches = engine.branches(turn)

    tic = tm.perf_counter()

    output_layer, octave_time = octave.feedforward_prop(branches_to_can_p(branches), board_to_X(engine.board, turn), dataset, nout=2)
    print(output_layer)
    toc = tm.perf_counter()
    print(toc - tic - octave_time, octave_time)

    return output_layer_to_move(branches, output_layer)


def game_turn(engine, turn, dataset1, dataset2):
    engine.move(nn_move(engine, turn, [dataset1, dataset2][int(turn)]))

    print("")
    engine.illustrate(True)
    print("")


def fight(dataset1, dataset2):
    engine = eg.engine_setup("regular")
    #$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"

    turn = True
    move_n = 1
    while True:
        game_turn(engine, turn, dataset1, dataset2)
        print("Move number ", move_n)
        move_n += 1
        win_lose_draw = engine.win_lose_draw()
        if win_lose_draw == 0 or is_stalemate(engine, turn, move_n) or move_n > 200:
            print("Draw")
            datasets = [dataset1, dataset2]
            if engine.eval() < 0:
                datasets.reverse()
                
            return datasets[0], datasets[1], False

        if win_lose_draw == 1000:
            print("White_wins")
            return dataset1, dataset2, True

        if win_lose_draw == -1000:
            print("Black_wins")
            return dataset2, dataset1, True

        turn = not turn 


print(fight(10,32))