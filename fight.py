import game as gm
# import numpy as np
# from oct2py import octave
import pieces as pc


def board_to_X(board, turn):
    X = [[[0] * 8] * 8] * 12
    types = [pc.Pawn, pc.Rook, pc.Knight, pc.Bishop, pc.Queen, pc.King]
    for piece in board.white_pieces.values():
        if piece.location is not None:
            X[types.index(type(piece))][piece.location[0]][piece.location[1]] = 1

    for piece in board.black_pieces.values():
        if piece.location is not None:
            X[types.index(type(piece)) + 6][piece.location[0]][piece.location[1]] = 1

    X.append(int(turn) * 2 - 1)

    return np.array(X)

            
def fight():
    game = gm.game_start()
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

