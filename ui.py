import game as gm
import numpy as np
from oct2py import octave


print("Welcome to chess engine ui. For help at any stage, smash your head on the keyboard and press enter.")
print("")

game = gm.game_start_nn()

theta = []
for x in range(1, 4):
    theta.append(np.array(octave.get_theta(1, x)))

game.engine.thetas.append(theta)

game.engine.depth = 1

print("")
game.illustrate()
print("")

if not game.user_colour:
    game.engine_turn()

while not game.concluded():
    game.user_turn()

    if not game.concluded():
        if game.engine_on:
            game.engine_turn()
        else:
            game.user_turn()

print("")
if game.white_win:
    print("White wins")

elif game.black_win:
    print("Black wins")

elif game.draw:
    print("Draw")

else:
    print("Stopped")