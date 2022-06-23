import game as gm


print("Welcome to chess engine ui. For help at any stage, smash your head on the keyboard and press enter.")
print("")

game = gm.game_start()

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