import fight as ft
from oct2py import octave
import shutil
import numpy as np
from statistical_significance import p
import time
import random


#$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"

def train(depth, examples, steps, thetas, _lambda, morph_rate):
    '''
    Trains the NN on the comb engine. {Depth} specifies the depth the comb engine runs on.
    '''
    octave.addpath("/home/joseph/Desktop/chess_neural_network")
    # shutil.copyfile(
    #     f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{thetas[0]}.mat', 
    #     f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{thetas[1]}.mat'
    # )

    theta_train = thetas[0]
    theta_morph = thetas[1]
    for i in range(steps):
        X_win = []
        y_win = []
        X_lose = []
        y_lose = []
        X_draw = []
        y_draw = []

        while len(y_win) < examples[0] or len(y_lose) < examples[1]:
            print(f"gen: {i + 1}")
            print(f"examples (w, l, d): {(len(y_win), len(y_lose), len(y_draw))}")

            thetas.reverse()
            # n = octave.morph(theta_morph, morph_rate)
            X_j, y_j = ft.fight_random_pos([thetas[0], thetas[1]])
            # shutil.copyfile(
            # f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{theta_train}.mat', 
            # f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{theta_morph}.mat'
            # )
            
            if y_j[0] == 1:
                X_win += X_j
                y_win += y_j

            elif y_j[0] == 0:
                X_lose += X_j
                y_lose += y_j

            else:
                X_draw += X_j
                y_draw += y_j

        for dataset in [X_win, X_lose, X_draw, y_win, y_lose, y_draw]:
            random.shuffle(dataset)

        for x in range(1, 9):
            n = octave.back_prop(
                x, 
                np.array(X_win[:examples[0]] + X_lose[:examples[1]] + X_draw[:min(len(X_draw), examples[2])]), 
                np.array(y_win[:examples[0]] + y_lose[:examples[1]] + y_draw[:min(len(y_draw), examples[2])]),
                _lambda
            )
        # shutil.copyfile(
        #     f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{theta_train}.mat', 
        #     f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{theta_morph}.mat'
        # )


def compete(thetas):
    '''
    Trains the NN on the comb engine. {Depth} specifies the depth the comb engine runs on.
    '''
    octave.addpath("/home/joseph/Desktop/chess_neural_network")
    win = 0
    lose = 0
    draw = 0

    while win < 100 and lose < 100:
        X_j, y_j = ft.fight_random_pos([thetas[0], thetas[1]])
        
        if y_j[0] == 1:
            win += 1

        elif y_j[0] == 0:
            lose += 1

        elif y_j[0] == 0.5:
            draw += 1

        print((win, lose, draw))
        p(max(win, lose), min(win, lose), 0.5)

    return win


    