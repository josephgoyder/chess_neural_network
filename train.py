import training as tr
import genetic_algorithm as ga
import shutil
import numpy as np
import fight


# theta_size = 50
# ga.theta_init(
#     np.array([770, theta_size]), 
#     np.array([theta_size + 1, theta_size]), 
#     np.array([theta_size + 1, 1]), 
#     100
# )

wins = 0
for theta in range(47, 101):
    winner, loser, irrelevant = fight.fight([1, theta])
    if winner == 1:
        wins += 1
    
    print(wins, theta)

# tr.compete([1, 2])
# ga.genetic_algorithm(20, 4, 100, 2, 2, 3, 20, 50)
# tr.train(1, (1000, 1000, 2000), 5, [1, 2], 0.01, 0.3)
