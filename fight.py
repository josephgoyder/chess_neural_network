from engine import Engine_regular, engine_setup
import game as gm
import pieces as pc
import eval as ev
import numpy as np

            
def train_assisted(depth):
    game = gm.game_start_nn()
    engine_comb = Engine_regular(
        game.engine.history, 
        game.engine.notebook, 
        game.engine.board, 
        depth,
        [1, 1],
        10.0, 
        1.0
    )

    game.engine.depth = 2

    X_comb = []
    y_comb = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()

        engine_comb.search(game.turn, depth, 1, engine_comb.branches(game.turn))
        move_comb = engine_comb.notebook.top_lines[0][1][0]
        for branch in game.engine.branches(game.turn):
            game.engine.move(branch, game.turn)
            X_comb.append(ev.board_to_X(game.engine.board, game.turn))
            y_comb.append(int((branch == move_comb) == game.turn))
            game.engine.undo()

        move_n += 1
        if move_n == 200:
            game.draw = True

        print("Move: ", move_n)

    print("")
    if game.white_win:
        print("White wins")
        eval = 1

    elif game.black_win:
        print("Black wins")
        eval = 0

    elif game.draw:
        print("Draw")
        eval = 0.5

    return X_comb, y_comb


def train_unassisted():
    game = gm.game_start_nn()

    game.engine.depth = 2

    X_nn = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()
        X_nn.append(ev.board_to_X(game.engine.board, game.turn))
        move_n += 1
        if move_n == 200:
            game.draw = True

        print("Move: ", move_n)

    print("")
    if game.white_win:
        print("White wins")
        eval = 1

    elif game.black_win:
        print("Black wins")
        eval = 0

    elif game.draw:
        print("Draw")
        eval = 0.5

    y_nn = [eval] * move_n 

    return X_nn, y_nn
