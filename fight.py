from zmq import THREAD_AFFINITY_CPU_ADD
from engine import Engine_regular, engine_setup
import game as gm
import pieces as pc
import eval as ev
import numpy as np
import random
from oct2py import octave


def fight(thetas):
    # init game and eval NN
    game = gm.game_start_nn()

    for theta_num in thetas:
        theta = []
        for x in range(1, 4):
            theta.append(np.array(octave.get_theta(theta_num, x)))

        game.engine.thetas.append(theta)

    game.engine.depth = 1

    move_n = 0
    while not game.concluded():
        game.engine_turn()
        game.engine.thetas.reverse()

        # increment move number and draw if move cap is reached
        move_n += 1
        if move_n == 200:
            game.draw = True

        print("Move: ", move_n)

    # show result of game and set eval for the NN training examples
    print("")
    if game.white_win:
        print("White wins")
        return thetas[0], thetas[1], True

    elif game.black_win:
        print("Black wins")
        return thetas[1], thetas[0], True

    elif game.draw:
        print("Draw")
        random.shuffle(thetas)
        return thetas[0], thetas[1], True
        

def fight_assisted(depth, thetas):
    '''
    Make the training set for the eval NN from one game. 
    Uses its own results and the move recommendation of the comb engine for the training set.
    '''
    
    # init comb engine and NN
    game = gm.game_start_nn()
    
    game.engine.depth = 1
    game.engine.random_eval = True

    for theta_num in thetas:
        theta = []
        for x in range(1, 4):
            theta.append(np.array(octave.get_theta(theta_num, x)))

        game.engine.thetas.append(theta)

    for x in range(random.randint(0, 20)):
        game.engine_turn()

    game.engine = Engine_regular(
        game.engine.history,
        game.engine.notebook,
        game.engine.board,
        depth,
        game.engine.top_lines_filters,
        10,
        1
    )

    # init training set and move count
    X_comb = []
    y_comb = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()
        X_comb.append(ev.board_to_X(game.engine.board, game.turn))
        
        # increment move number and draw if move cap is reached
        move_n += 1
        if move_n == 200:
            game.draw = True

        print("Move: ", move_n)

    # show result of game and set eval for the NN training examples
    print("")
    if game.white_win:
        print("White wins")
        y_comb = [x / (2 * move_n) for x in range(move_n, 2 * move_n)]

    elif game.black_win:
        print("Black wins")
        y_comb = [x / (2 * move_n) for x in range(move_n, 0, -1)]

    elif game.draw:
        print("Draw")
        y_comb = [0.5] * move_n 

    return X_comb, y_comb


def fight_unassisted(thetas):
    '''
    Make the training set for the eval NN from one game. 
    Uses its own results for the training set.
    '''

    # init game and eval NN
    game = gm.game_start_nn()

    for theta_num in thetas:
        theta = []
        for x in range(1, 4):
            theta.append(np.array(octave.get_theta(theta_num, x)))

        game.engine.thetas.append(theta)

    game.engine.depth = 1

    # init X for the training set and move number
    X_nn = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()
        game.engine.thetas.reverse()

        # add board state to training set
        X_nn.append(ev.board_to_X(game.engine.board, game.turn))

        # increment move number and draw if move cap is reached
        move_n += 1
        if move_n == 200:
            game.draw = True

        print("Move: ", move_n)

    # show result of game and set eval for the NN training examples
    print("")
    if game.white_win:
        print("White wins")
        y_nn = [x / (2 * move_n) for x in range(move_n, 2 * move_n)]

    elif game.black_win:
        print("Black wins")
        y_nn = [x / (2 * move_n) for x in range(move_n, 0, -1)]

    elif game.draw:
        print("Draw")
        y_nn = [0.5] * move_n 

    return X_nn, y_nn


def fight_random_pos(thetas):
    # init game and eval NN
    game = gm.game_start_nn()

    for theta_num in thetas:
        theta = []
        for x in range(1, 4):
            theta.append(np.array(octave.get_theta(theta_num, x)))

        game.engine.thetas.append(theta)

    game.engine.depth = 1
    game.engine.random_eval = True

    for x in range(random.randint(0, 20)):
        game.engine_turn()
        game.engine.thetas.reverse()

    game.engine.random_eval = False

    # init X for the training set and move number
    X_nn = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()
        game.engine.thetas.reverse()
        # add board state to training set
        X_nn.append(ev.board_to_X(game.engine.board, game.turn))

        # increment move number and draw if move cap is reached
        move_n += 1
        
        if move_n == 200:
            game.draw = True

        print("Move: ", move_n)

    # show result of game and set eval for the NN training examples
    print("")
    if game.white_win:
        print("White wins")
        y_nn = [x / (2 * move_n) for x in range(move_n, 2 * move_n)]

    elif game.black_win:
        print("Black wins")
        y_nn = [x / (2 * move_n) for x in range(move_n, 0, -1)]

    elif game.draw:
        print("Draw")
        y_nn = [0.5] * move_n 

    return X_nn, y_nn