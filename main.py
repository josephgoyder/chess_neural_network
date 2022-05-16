from oct2py import octave
#import fight 
import numpy as np

def theta_init(Theta_1_size, Theta_2_size, Theta_3_size, n):

    octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")
    #\\Users\\076-jgoyder\\Chess engine\\chess_neural_network
    #A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network
    n = octave.rand_init_thetas(Theta_1_size, Theta_2_size, Theta_3_size, n)


def tournament(generation, population):
    
    winner_list = []
    for i in population / 2:
        winner = fight(i, i*2)
        winner_list.append(winner)

# def reproduction():
#     octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")

# def mutation():


def main():

    generation = 5

    theta_init(np.array([98, 500.]), np.array([501, 500.]), np.array([501, 850.]), 2*generation - 1)

    # for i in generation:
    #     living_player = 2 ** (generation - i - 1)
    #     tournament(living_player)
    #     reproduction(living_player)
    #     mutaion(living_player)

main()


