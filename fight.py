from engine import Engine_regular, engine_setup
import game as gm
import pieces as pc
import eval as ev
import numpy as np
import random
from oct2py import octave

            
def fight_assisted(depth, thetas):
    '''
    Make the training set for the eval NN from one game. 
    Uses its own results and the move recommendation of the comb engine for the training set.
    '''
    
    # init comb engine and NN
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
    game.engine.random_eval = True

    # init training set and move count
    X_comb = []
    y_comb = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()

        # get engine move recommendation {move_comb}
        # engine_comb.notebook.top_lines.clear()
        # engine_comb.search(game.turn, depth, 1, engine_comb.branches(game.turn))
        
        X_comb.append(ev.board_to_X(game.engine.board, game.turn))
        y_comb.append(octave.sigmoid(engine_comb.eval(game.turn) / 100))

        # increment move number and draw if move cap is reached
        move_n += 1
        if move_n == 100:
            game.draw = True

        print("Move: ", move_n)

    # show result of game and set eval for the NN training examples
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


def fight_unassisted(thetas):
    '''
    Make the training set for the eval NN from one game. 
    Uses its own results for the training set.
    '''

    # init game and eval NN
    game = gm.game_start_nn()

    game.engine.depth = 2
    game.engine.thetaset = thetas[int(not game.turn)]

    # init X for the training set and move number
    X_nn = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()

        # add board state to training set
        X_nn.append(ev.board_to_X(game.engine.board, game.turn))

        # increment move number and draw if move cap is reached
        move_n += 1
        game.engine.thetaset = thetas[int(not game.turn)]
        if move_n == 200:
            game.draw = True

        print("Move: ", move_n)

    # show result of game and set eval for the NN training examples
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


def fight_random_pos(thetas):
    # init game and eval NN
    game = gm.game_start_nn()

    game.engine.depth = 2
    game.engine.random_eval = True

    for x in range(random.randint(0, 20)):
        game.engine_turn()

    game.engine.thetaset = thetas[int(not game.turn)]
    game.engine.random_eval = False

    # init X for the training set and move number
    X_nn = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()

        # add board state to training set
        X_nn.append(ev.board_to_X(game.engine.board, game.turn))

        # increment move number and draw if move cap is reached
        move_n += 1
        game.engine.thetaset = thetas[int(not game.turn)]
        if move_n == 200:
            game.draw = True

        print("Move: ", move_n)

    # show result of game and set eval for the NN training examples
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