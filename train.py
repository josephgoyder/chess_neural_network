import training as tr
import genetic_algorithm as ga
import shutil
import numpy as np
from statistical_significance import p
import fight
import random


# theta_size = 50
# ga.theta_init(
#     np.array([770, theta_size]), 
#     np.array([theta_size + 1, theta_size]), 
#     np.array([theta_size + 1, 1]), 
#     8
# )

# wins = 0
# for theta in range(1, 101):
#     winner, loser, irrelevant = fight.fight([200, theta])
#     if winner == 200:
#         wins += 1
    
#     print(wins, theta)
#     p(wins, theta - wins, 0.5)

tr.compete([1, 2])
# ga.genetic_algorithm(60, 4, 30, 7, 3, 20, 50, self_training=True)

# tr.train(1, (1000, 1000, 2000), 1, [theta1, theta2], 0.01, 0.3)
