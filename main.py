from oct2py import octave
import fight 
import numpy as np
import os

def theta_init(Theta_1_size, Theta_2_size, Theta_3_size, n):

    octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")
    #\\Users\\076-jgoyder\\Chess engine\\chess_neural_network
    #A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network
    n = octave.rand_init_thetas(Theta_1_size, Theta_2_size, Theta_3_size, n)


def tournament(generation, population):
    
    for i in range(int(population / 2)):
        i += 1
        i *= 2
        winner, loser = fight.fight(i, i - 1)
        os.remove(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{loser}.mat")
        os.rename(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{winner}.mat", f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{i//2}.mat")

    

def reproduction(population):
    octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")
    for datasets in range(population // 4):
        dataset_1 = (datasets + 1) * 2
        dataset_2 = dataset_1 - 1
        n = octave.reproduction(dataset_1, dataset_2)


# def mutation(population):
#     for dataset in range(population):
#         n = octave.mutation(dataset)

def main():

    generations = 4
    population = 2 ** (generations - 1)
    theta_init(np.array([98, 50.]), np.array([51, 50.]), np.array([51, 850.]), population)

    for generation in range(generations):
        population = (generation - 1) ** 2
        tournament(generation, population)
        reproduction(population)
        # mutaion(population)

main()


