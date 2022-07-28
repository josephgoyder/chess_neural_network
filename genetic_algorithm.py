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
    n = octave.random_init_weights(Theta_1_size, Theta_2_size, Theta_3_size, n)


def tournament(rounds):
    for r in range(rounds):
        population = len(os.listdir('/home/joseph/Desktop/chess_neural_network/engine_data'))
        for i in range((population // 2)):
            i = (i + 1) * 2

            print(i, " vs ", (i - 1))

            winner, loser, win_state = fight.fight([i, i - 1])
            os.remove(f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{loser}.mat")
            os.rename(f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{winner}.mat", f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{i//2}.mat")


def multi_tournament(heats, survivor_num):

    population = len(os.listdir('/home/joseph/Desktop/chess_neural_network/engine_data'))
    print("Current population: ", population)

    players = list(range(1, population + 1))
    fight_sequense = list(players)
    random.shuffle(fight_sequense)
    fight_info = {players[i]: 0 for i in range(len(fight_sequense))}

    for heat in range(heats):
        for round in range(population):
            player_1 = fight_sequense[round]
            player_2 = fight_sequense[(round + heat + 1) % population]
            
            print(player_1, " vs ", player_2)
            print(f"Heat: {heat + 1} / {heats}")
            print(f"Round: {round + 1} / {population}")

            winner, loser, win_state = fight.fight([player_1, player_2])

            if win_state:
                fight_info[winner] += 1
                fight_info[loser] -= 1
            else:
                fight_info[winner] += 0.1
                fight_info[loser] -= 0.1
    
    print(fight_info)

    strongest = max(fight_info, key = fight_info.get)
    folder = '/home/joseph/Desktop/chess_neural_network/elite_data/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    if strongest != 1:
        shutil.copyfile(f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{strongest}.mat', 
                        f'/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{1}.mat'
    )
    
    players.sort(key = lambda player: fight_info[player], reverse = True)
    survivors = players[:survivor_num]
    death = players[survivor_num:]
    
    print(survivors)
    print("number of survivors: ", len(survivors))

    for player in death:
        os.remove(f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{player}.mat")
    
    survivors.sort()
    n = 1
    for player in survivors:
        os.rename(f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{player}.mat", f"/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_{n}.mat")
        n += 1
    
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


def reproduction(population):
    octave.addpath("/home/joseph/Desktop/chess_neural_network")
    for datasets in range(population // 4):
        dataset_1 = (datasets + 1) * 2
        dataset_2 = dataset_1 - 1
        n = octave.reproduction(dataset_1, dataset_2, dataset_1, dataset_2)

def multi_reproduction(goal_population):

    current_population = 0

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
    
    population = len(os.listdir('/home/joseph/Desktop/chess_neural_network/parent_engine_data/'))
    while current_population < goal_population:

        parent_1 = random.randint(1, population)

        parent_2 = random.randint(1, population)
        while parent_2 == parent_1:
            parent_2 = random.randint(1, population)

        n = octave.reproduction_single(parent_1, parent_2, current_population + 1)
        current_population += 1


def mutation(mutation_rate):

    allfiles = os.listdir('/home/joseph/Desktop/chess_neural_network/engine_data/')
    population = len(allfiles)

    for dataset in range(population//2):
        n = octave.mutation(dataset + 1, mutation_rate)

def generation_sequence(heats, survivor_num, goal_population, mutation_rate):
    multi_tournament(heats, survivor_num)
    multi_reproduction(goal_population)
    mutation(mutation_rate)
    source = '/home/joseph/Desktop/chess_neural_network/elite_data/'
    destination = '/home/joseph/Desktop/chess_neural_network/engine_data/'
  
    allfiles = os.listdir(source)
  
    for f in allfiles:
        shutil.move(source + f, destination + f)
    
def genetic_algorithm(population, survivor_num, generations, descend_generations, heats, mutation_rate, theta_size):

    tic = time.perf_counter()
    theta_init(np.array([770, theta_size]), np.array([theta_size + 1, theta_size]), np.array([theta_size + 1, 1.]), population)
    octave.addpath("/home/joseph/Desktop/chess_neural_network")

    for i in range(generations - 1):
        print(f"Gen: {i + 1} / {generations}")
        generation_sequence(heats, survivor_num, population, mutation_rate) 

    descend_init_population = 2 ** (descend_generations - 1)
    print(f"Gen: {generations} / {generations}")
    generation_sequence(heats, survivor_num, descend_init_population, mutation_rate)
    
    tournament(descend_generations)

    toc = time.perf_counter()
    print(toc - tic)