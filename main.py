from oct2py import octave
import fight 
import numpy as np
import os
import random
import time
import shutil

def theta_init(Theta_1_size, Theta_2_size, Theta_3_size, n):

    octave.addpath("/home/joseph/Desktop/chess_neural_network")

    folder = '/home/joseph/Desktop/chess_neural_network/engine_data/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    #\\Users\\076-jgoyder\\Chess engine\\chess_neural_network
    #A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network
    n = octave.rand_init_thetas(Theta_1_size, Theta_2_size, Theta_3_size, n)


def tournament():
    population = len(allfiles = os.listdir('/home/joseph/Desktop/chess_neural_network/engine_data'))
    for i in range((population // 2)):
        i = (i + 1) * 2

        print(i, " vs ", (i - 1))

        winner, loser, win_state = fight.fight(i, i - 1)
        os.remove(f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{loser}.mat")
        os.rename(f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{winner}.mat", f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{i//2}.mat")


def multi_tournament(heats, survivability, min_player):

    population = len(os.listdir('/home/joseph/Desktop/chess_neural_network/engine_data'))
    print("Current population: ", population)

    fight_sequense = list(range(1, population + 1))
    fight_info = {fight_sequense[i]: 0 for i in range(len(fight_sequense))}

    for heat in range(heats):
        for round in range(population):
            player_1 = fight_sequense[round]
            
            if (round + (2 ** heat)) < population:
                player_2 = fight_sequense[round + (2 ** heat)]
            else:
                player_2 = fight_sequense[round + (2 ** heat) - population]
            
            print(player_1, " vs ", player_2)

            winner, loser, win_state = fight.fight(player_1, player_2)

            if win_state:
                fight_info[winner] += 1
                fight_info[loser] -= 1
            else:
                fight_info[winner] += 0.5
                fight_info[loser] -= 0.5
    
    print(fight_info)

    survivors = []
    death = []

    result_population = 0
    for player in fight_info:
        if fight_info[player] < survivability:
            death.append(player)
        else:
            survivors.append(player)
            result_population += 1
    
    while result_population < min_player:
        n = 1
        for player in death:
            if fight_info[player] == (survivability - n):
                death.remove(player)
                survivors.append(player)
        n += 1
    
    for player in death:
        os.remove(f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{player}.mat")
    
    n = 1
    for player in survivors:
        os.rename(f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{player}.mat", f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{n}.mat")
        n += 1

def reproduction(population):
    octave.addpath("/home/joseph/Desktop/chess_neural_network")
    for datasets in range(population // 4):
        dataset_1 = (datasets + 1) * 2
        dataset_2 = dataset_1 - 1
        n = octave.reproduction(dataset_1, dataset_2, dataset_1, dataset_2)


def multi_reproduction(goal_population):
    
    folder = '/home/joseph/Desktop/chess_neural_network/parent_engine_data/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    source = '/home/joseph/Desktop/chess_neural_network/engine_data/'
    destination = '/home/joseph/Desktop/chess_neural_network/parent_engine_data/'
  
    allfiles = os.listdir(source)
    population = len(allfiles)
    print("Population: ", population)
  
    for f in allfiles:
        shutil.move(source + f, destination + f)

    current_population = 0

    while current_population < goal_population:

        parent_1 = random.randint(1, population)

        parent_2 = random.randint(1, population)
        while parent_2 == parent_1:
            parent_2 = random.randint(1, population)

        n = octave.reproduction_single(parent_1, parent_2, current_population + 1)
        current_population += 1


def mutation(population, mutation_rate):
    for dataset in range(population//2):
        n = octave.mutation(dataset + 1, mutation_rate)

def main(init_population, elite_size, descend_generations):

    tic = time.perf_counter()
    theta_init(np.array([98, 150.]), np.array([151, 150.]), np.array([151, 850.]), init_population)
    octave.addpath("/home/joseph/Desktop/chess_neural_network")

    #Genetic algorithm sequence

    for i in range(4):
        multi_tournament(4, 4, 8)
        multi_reproduction(100)
    
    # for i in range(2):
    #     multi_tournament(3, 4, 6)
    #     multi_reproduction(init_population)
    
    # for i in range(2):
    #     multi_tournament(4, 7, 6)
    #     multi_reproduction(elite_size)
    
    # multi_tournament(4, 7, 6)

    # descend_init_population = 2 ** (descend_generations - 1)
    # multi_reproduction(descend_init_population)
    
    # for generation in range(descend_generations - 2):
    #     current_generation = descend_generations - generation
    #     if current_generation > 4:
    #         multi_tournament(3, 4, 6)
    #         multi_reproduction(2 ** (current_generation - 1))
    #     elif current_generation <= 4 and current_generation > 2:
    #         multi_tournament(2, 2, 4)
    #         multi_reproduction(2 ** (current_generation - 1))

    #     elif current_generation == 2:
    #         tournament()

    # toc = time.perf_counter()

    # print(toc - tic)

main(400, 16, 16)