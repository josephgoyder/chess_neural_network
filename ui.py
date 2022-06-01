import game as gm

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