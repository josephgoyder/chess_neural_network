import fight as ft
from oct2py import octave
import shutil
import numpy as np
import time


#$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"

def train(depth, games_per_step, thetas, _lambda):
    '''
    Trains the NN on the comb engine. {Depth} specifies the depth the comb engine runs on.
    '''
    octave.addpath("/home/joseph/Desktop/chess_neural_network")
    for i in range(1):
        print(f"gen: {i + 1}")
        
        X = []
        y = []
        for j in range(games_per_step):
            print(f"game: {j + 1}")
            # n = octave.morph(2, 0.3)
            X_j, y_j = ft.train_assisted(depth)
            X += X_j
            y += y_j
            # shutil.copyfile('/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_1.mat', '/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_2.mat')

        for theta in thetas:
            n = octave.back_prop(theta, np.array(X), np.array(y), _lambda)
        # shutil.copyfile('C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_1.mat', '/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_2.mat')

        # set dataset 2 to dataset 1


