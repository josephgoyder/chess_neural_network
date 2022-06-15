from engine import Engine_regular, engine_setup
import game as gm
import pieces as pc
import eval as ev
import numpy as np

            
def fight():
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

    X_nn = []
    X_comb = []
    y_comb = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()
        X_nn.append(ev.board_to_X(game.engine.board, game.turn))

        engine_comb.explore(game.turn)
        move_comb = engine_comb.notebook.top_lines[0][1][0]
        for branch in game.engine.branches():
            game.engine.move(branch, game.turn)
            X_comb.append(ev.board_to_X(game.engine.board, game.turn))
            y_comb.append(branch == move_comb)
            game.engine.undo()

        move_n += 1
        if move_n == 200:
            game.draw = True

        print("Move: ", move_n)
        print("X size:", np.shape(X))

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

    return np.array(X), np.array(y)

