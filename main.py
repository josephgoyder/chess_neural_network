from oct2py import octave
import fight 
import numpy as np
import time as tm

def theta_init(Theta_1_size, Theta_2_size, Theta_3_size, n):

    octave.addpath("\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\rand_init_thetas.m")
    octave.rand_init_thetas(Theta_1_size, Theta_2_size, Theta_3_size, n)

theta_init(np.array([98, 500]), np.array([501, 500]), np.array([501, 242]), 100)

