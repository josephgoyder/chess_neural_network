from engine import Engine_regular, engine_setup
import game as gm
import pieces as pc
import eval as ev
import numpy as np

            
def train_assisted():
    game = gm.game_start_nn()
    engine_comb = Engine_regular(
        game.engine.history, 
        game.engine.notebook, 
        game.engine.board, 
        4,
        [1, 1],
        10.0, 
        1.0
    )

    game.engine.depth = 2

    X_nn = []
    X_comb = []
    y_comb = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()
        X_nn.append(ev.board_to_X(game.engine.board, game.turn))

        engine_comb.explore(game.turn)
        move_comb = engine_comb.notebook.top_lines[0][1][0]
        y_comb.append(int(game.turn))

        game.engine.move(move_comb, game.turn)
        X_comb.append(ev.board_to_X(game.engine.board, game.turn))
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

    y_nn = [eval] * move_n 

    return np.array(X_nn + X_comb), np.array(y_nn + y_comb)


def train():
    game = gm.game_start()

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

    return np.array(X_nn), np.array(y_nn)
