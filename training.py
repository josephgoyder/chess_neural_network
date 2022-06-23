import fight as ft
from oct2py import octave
import shutil
import numpy as np
import time


#$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"

def train(depth, games_per_step, theta):
    '''
    Trains the NN on the comb engine. {Depth} specifies the depth the comb engine runs on.
    '''
    octave.addpath("/home/joseph/Desktop/chess_neural_network")
    for i in range(10):
        print(f"gen: {i}")
        n = octave.mutation(2, 30)
        X = []
        y = []
        for j in range(games_per_step):
            X_j, y_j = ft.train_unassisted()
            X += X_j
            y += y_j

        n = octave.back_prop(theta, np.array(X), np.array(y), 1)
        shutil.copyfile('/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_1.mat', '/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_2.mat')
        # shutil.copyfile('C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_1.mat', '/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_2.mat')

        # set dataset 2 to dataset 1

train(1, 1, 1)


