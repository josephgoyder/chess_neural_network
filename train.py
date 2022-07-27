import training as tr
import genetic_algorithm as ga
import shutil
import numpy as np
import fight

wins = 0
for theta in range(2, 101):
    winner, loser, irrelevant = fight.fight([1, theta])
    if winner == 1:
        wins += 1

print(wins)

# tr.compete([1, 2])
# ga.genetic_algorithm(100, 5, 3, 3, 2, 3, 20, 50)

# theta_size = 50
# ga.theta_init(
#     np.array([770, theta_size]), 
#     np.array([theta_size + 1, theta_size]), 
#     np.array([theta_size + 1, 1]), 
#     100
# )
# tr.train(1, (1000, 1000, 2000), 5, [1, 2], 0.01, 0.3)
