from oct2py import octave
import fight 
import numpy as np
import os
import random
import time
import shutil

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


def tournament():
    population = len(allfiles = os.listdir('A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data'))
    for i in range((population // 2)):
        i = (i + 1) * 2

        print(i, " vs ", (i - 1))

        winner, loser, win_state = fight.fight(i, i - 1)
        os.remove(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{loser}.mat")
        os.rename(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{winner}.mat", f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{i//2}.mat")


def multi_tournament(heats, survivability):

    population = len(allfiles = os.listdir('A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data'))

    fight_sequense = [i for i in range(1, population + 1)]
    random.shuffle(fight_sequense)
    fight_info = {fight_sequense[i]: 0 for i in range(len(fight_sequense))}

    for heat in range(heats):
        for round in range(population):
            player_1 = fight_sequense[round]
            
            if (round + 2 ** heat) < population:
                player_2 = fight_sequense[round + 2 ** heat]
            else:
                player_2 = fight_sequense[round + 2 ** heat - population]

            winner, loser, win_state = fight.fight(player_1, player_2)

            if win_state:
                fight_info[winner] += 1
                fight_info[loser] -= 1
    
    result_population = 1
    for player in fight_sequense:
        if fight_info[player] < survivability:
            os.remove(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{fight_sequense[player]}.mat")
        else:
            os.rename(f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{fight_sequense[player]}.mat", f"A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_{result_population}.mat")
            result_population += 1

    return result_population


def reproduction(population):
    octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")
    for datasets in range(population // 4):
        dataset_1 = (datasets + 1) * 2
        dataset_2 = dataset_1 - 1
        n = octave.reproduction(dataset_1, dataset_2, dataset_1, dataset_2)


def multi_reproduction(goal_population):
    
    source = 'A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data'
    destination = 'A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\parent_engine_data'
  
    allfiles = os.listdir(source)
    population = len(allfiles)
  
    for f in allfiles:
        shutil.move(source + f, destination + f)

    current_population = 0
    while current_population < goal_population:
        parent_1 = random.randint(1, population + 1)
        parent_2 = random.randint(1, population + 1)
        n = octave.reproduction_single(parent_1, parent_2, current_population + 1)
        current_population += 1


def mutation(population, mutation_rate):
    for dataset in range(population//2):
        n = octave.mutation(dataset + 1, mutation_rate)

def main(init_population, elite_size, descend_generations):

    tic = time.perf_counter()
    theta_init(np.array([98, 50.]), np.array([51, 50.]), np.array([51, 850.]), init_population)
    octave.addpath("A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network")
    
    for i in range(2):
        multi_tournament(3, 4)
        multi_reproduction(init_population)
    
    for i in range(2):
        multi_tournament(4, 7)
        multi_reproduction(elite_size)
    
    multi_tournament(4, 7)

    descend_init_population = 2 ** (descend_generations - 1)
    multi_reproduction(descend_init_population)
    
    for generation in range(descend_generations - 2):
        current_generation = descend_generations - generation
        if current_generation > 4:
            multi_tournament(3, 4)
            multi_reproduction(2 ** (current_generation - 1))
        elif current_generation <= 4 and current_generation > 2:
            multi_tournament(2, 2)
            multi_reproduction(2 ** (current_generation - 1))

        elif current_generation == 2:
            tournament()

    toc = time.perf_counter()

    print(toc - tic)

main(6)