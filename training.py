import fight as ft
from oct2py import octave
import shutil
import numpy as np
import time
import random


#$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"

def train(depth, examples, steps, thetas, _lambda, morph_rate):
    '''
    Trains the NN on the comb engine. {Depth} specifies the depth the comb engine runs on.
    '''
    octave.addpath("/home/joseph/Desktop/chess_neural_network")
    shutil.copyfile(f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{thetas[0]}.mat', f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{thetas[1]}.mat')
    for i in range(steps):
        X_win = []
        y_win = []
        X_lose = []
        y_lose = []
        X_draw = []
        y_draw = []

        while len(y_win) < examples[0] or len(y_lose) < examples[1] or len(y_draw) < examples[2]:
            print(f"gen: {i + 1}")
            print(f"examples (w, l, d): {(len(y_win), len(y_lose), len(y_draw))}")
            X_j, y_j = ft.fight_unassisted([thetas[0], thetas[1]])
            
            if y_j[0] == 1:
                X_win += X_j
                y_win += y_j

            elif y_j[0] == 0:
                X_lose += X_j
                y_lose += y_j

            elif y_j[0] == 0.5:
                X_draw += X_j
                y_draw += y_j

        for dataset in [X_win, X_lose, X_draw, y_win, y_lose, y_draw]:
            random.shuffle(dataset)

        n = octave.back_prop(thetas[0], np.array(X_win[:examples[0]] + X_lose[:examples[1]] + X_draw[:examples[2]]), np.array(y_win[:examples[0]] + y_lose[:examples[1]] + y_draw[:examples[2]]), _lambda)
        shutil.copyfile(f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{thetas[0]}.mat', f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{thetas[1]}.mat')
