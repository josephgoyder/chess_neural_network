from oct2py import octave
import fight 
import numpy as np
import os
import random
import time

def theta_init(Theta_1_size, Theta_2_size, Theta_3_size, n):

    octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")
    #\\Users\\076-jgoyder\\Chess engine\\chess_neural_network
    #A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network
    n = octave.rand_init_thetas(Theta_1_size, Theta_2_size, Theta_3_size, n)

def new_theta_init(Theta_1_size, Theta_2_size, Theta_3_size, population):

    octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")
    
    datasets = 0

    while datasets < population:
        a = octave.special_init_thetas(Theta_1_size, Theta_2_size, Theta_3_size, 2)
        winner, loser, win_state = fight.fight(1.2, 2.2)
        if win_state:
            os.remove(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{loser}.mat")
            os.rename(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{winner}.mat", f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{datasets + 1}.mat")
            datasets += 1


def tournament(population):
    
    for i in range((population // 2)):
        i = (i + 1) * 2

        print(i, " vs ", (i - 1))

        winner, loser, win_state = fight.fight(i, i - 1)
        os.remove(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{loser}.mat")
        os.rename(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{winner}.mat", f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{i//2}.mat")


def multi_tournament(population, heats):

    fight_sequense = random.shuffle(range(1, population + 1))
    fight_info = {fight_sequense[i]: 0 for i in range(len(fight_sequense))}

    for heat in heats:
        for round in range(population):
            player_1 = fight_sequense[round]
            
            if round + 2 ** heat < population:
                player_2 = fight_sequense[round + 2 ** heat]
            else:
                player_2 = fight_sequense[round + 2 ** heat - population]

            winner, loser, win_state = fight.fight(player_1, player_2)

            if win_state:
                



def reproduction(population):
    octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")
    for datasets in range(population // 4):
        dataset_1 = (datasets + 1) * 2
        dataset_2 = dataset_1 - 1
        n = octave.reproduction(dataset_1, dataset_2)


def mutation(population, mutation_rate):
    for dataset in range(population//2):
        n = octave.mutation(dataset + 1, mutation_rate)

def main(generations):

    tic = time.perf_counter()
    population = 2 ** (generations - 1)
    theta_init(np.array([98, 50.]), np.array([51, 50.]), np.array([51, 850.]), population)
    octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")

    for generation in range(generations - 2):
        population = 2 ** (generations - generation - 1)
        print("Current population: ", population)
        tournament(population)
        reproduction(population)
        mutation(population, 1000)
    
    tournament(2)

    toc = time.perf_counter()

    print(toc - tic)

main(8)