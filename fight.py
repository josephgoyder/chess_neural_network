import engine as eg
import comb_engine as cb_eg
import numpy as np
from oct2py import octave
import random
import time as tm
import move_undo as mo_un
import comb_move_undo as cb_mo_un
import pieces as pc
import comb_pieces as cb_pc


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


def game_turn_nn(engine_nn, engine_cb, turn, dataset1, dataset2, engine_choices, move_n):
    engine_nn.move(nn_move(engine_nn, turn, [dataset1, dataset2][int(turn)]))

    print("")
    engine_nn.illustrate(True)
    print("")


def nn_branches_first_move(nn_branches):
    for move in nn_branches:
        if type(move) == dict:
            return move


def move_cb_to_nn(move_cb, nn_branches, engine_nn, engine_cb):
    for move_nn in nn_branches:
        if type(move_nn) == dict and cb_mo_un.notation(move_cb, engine_cb.board) == mo_un.notation(move_nn, engine_nn.board):
            return move_nn

    print("No move found.")
    return nn_branches_first_move(nn_branches)

            
def game_turn_comb_engine_train_nn(engine_nn, engine_cb, turn, dataset1, dataset2, engine_choices, move_n):
    engine_cb.notebook.top_lines.clear()
    engine_cb.search(turn, 2, 5, engine_cb.branches(turn))
    nn_branches = engine_nn.branches(turn)
    
    if move_n <= 10:
        engine_choice = engine_choices[move_n - 1]
    else:
        engine_choice = 0

    move_cb = engine_cb.notebook.top_lines[engine_choice][1][0]
    move_nn = move_cb_to_nn(move_cb, nn_branches, engine_nn, engine_cb)

    

    engine_nn.move(move_nn)
    engine_cb.move(move_cb)

    print(cb_mo_un.notation(move_cb, engine_cb.board))

    print("")
    engine_cb.illustrate(True)
    print("")

    X = board_to_X(engine_cb.board, turn)
    y = np.array([branch == move_nn for branch in nn_branches])
    print("training...")
    J = octave.back_prop(1, X, y, 1, branches_to_can_p(engine_nn.branches(turn)))

def fight(dataset1, dataset2, mode = "GA", engine_choices = [0] * 10):
    engine_nn = eg.engine_setup("regular")
    engine_cb = cb_eg.engine_setup("regular")

    if mode == "GA":
        game_turn = game_turn_nn

    elif mode == "Training":
        game_turn = game_turn_comb_engine_train_nn

    #$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"
    turn = True
    move_n = 1
    while True:
        game_turn(engine_nn, engine_cb, turn, dataset1, dataset2, engine_choices, move_n)
        print("Move number ", move_n)
        move_n += 1
        win_lose_draw = engine_nn.win_lose_draw()
        if win_lose_draw == 0 or is_stalemate(engine_nn, turn, move_n) or move_n > 200:
            print("Draw")
            datasets = [dataset1, dataset2]
            if engine_nn.eval() < 0:
                datasets.reverse()
                
            return datasets[0], datasets[1], False

        if win_lose_draw == 1000:
            print("White_wins")
            return dataset1, dataset2, True

        if win_lose_draw == -1000:
            print("Black_wins")
            return dataset2, dataset1, True

        turn = not turn 
