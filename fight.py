import game as gm
import pieces as pc
import eval as ev

            
def fight():
    game = gm.game_start_nn()
    X = []
    move_n = 0

    while not game.concluded():
        game.engine_turn()
        # X.append(board_to_X(game.engine.board, game.turn))
        move_n += 1

    print("")
    if game.white_win:
        print("White wins")
        eval = 1

    elif game.black_win:
        print("Black wins")
        eval = 0

    elif game.draw:
        print("Draw")
        eval = 0.5

    y = [eval] * move_n 

