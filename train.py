import training as tr
import genetic_algorithm as ga
import shutil
import numpy as np
from statistical_significance import p
import fight
import random


# layer_1 = 150
# layer_2 = 25
# ga.theta_init(
#     np.array([770, layer_1]), 
#     np.array([layer_1 + 1, layer_2]), 
#     np.array([layer_2 + 1, 1]), 
#     2
# )

# wins = 0
# for theta in range(1, 101):
#     winner, loser, irrelevant = fight.fight([200, theta])
#     if winner == 200:
#         wins += 1
    
#     print(wins, theta)
#     p(wins, theta - wins, 0.5)

# tr.compete([3, 2])
ga.genetic_algorithm(160, 160, 1000, 0, 10, 0, 150, 25, self_training=True)
# tr.train(1, (1000, 1000, 2000), 30, [1, 2], 0.01, 0.3)
