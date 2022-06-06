import comb_board as bd
import comb_pieces as pc


def move_regular(board, move):
    if move["first_move"]:
        move["piece_1"].moved = True

    if move["en_passant_expire"]:
        move["piece_1"].en_passant_able = False

    move["piece_1"].location = move["location_2"]
    if move["piece_2"] is not None:
        move["piece_2"].location = None

    board.squares[move["location_2"][0]][move["location_2"][1]].piece = move[
        "piece_1"
    ]
    board.squares[move["location_1"][0]][move["location_1"][1]].piece = None


def move_en_passant(board, move):
    move["piece_2"].location = None
    board.squares[move["location_2"][0]][move["location_2"][1]].piece = None

    move_regular(
        board,
        {
            "location_1": move["location_1"],
            "location_2": move["location_3"],
            "piece_1": move["piece_1"],
            "piece_2": None,
            "first_move": False,
            "en_passant_expire": False
        },
    )


def move_promotion(board, move):
    if move["promotion"] == "queen":
        move["piece_1"] = pc.Queen(move["location_1"], move["piece_1"].colour)

    elif move["promotion"] == "knight":
        move["piece_1"] = pc.Knight(move["location_1"], move["piece_1"].colour)

    elif move["promotion"] == "bishop":
        move["piece_1"] = pc.Bishop(move["location_1"], move["piece_1"].colour)

    else:
        move["piece_1"] = pc.Rook(move["location_1"], move["piece_1"].colour)

    move_regular(board, move)


def move(move, board):
    if move["type"] == "regular":
        move_regular(board, move)

    elif move["type"] == "castle":
        move_regular(board, move["king_move"])
        move_regular(board, move["rook_move"])

    elif move["type"] == "promotion":
        move_promotion(board, move)

    elif move["type"] == "double_push":
        move_regular(board, move)
        move["piece_1"].en_passant_able = True

    else:
        move_en_passant(board, move)

    if move["piece_2"] is not None:
            board.change_piece_num(-1, move["piece_2"].colour)


def undo_regular(board, move):
    if move["first_move"]:
        move["piece_1"].moved = False

    if move["en_passant_expire"]:
        move["piece_1"].en_passant_able = True

    move["piece_1"].location = move["location_1"]
    if move["piece_2"] is not None:
        move["piece_2"].location = move["location_2"]
        board.squares[move["location_2"][0]][move["location_2"][1]].piece = move[
            "piece_2"
        ]

    else:
        board.squares[move["location_2"][0]][move["location_2"][1]].piece = None

    board.squares[move["location_1"][0]][move["location_1"][1]].piece = move[
        "piece_1"
    ]


def undo_en_passant(board, move):
    move["piece_2"].location = move["location_2"]
    board.squares[move["location_2"][0]][move["location_2"][1]].piece = move[
        "piece_2"
    ]

    undo_regular(
        board,
        {
            "location_1": move["location_1"],
            "location_2": move["location_3"],
            "piece_1": move["piece_1"],
            "piece_2": None,
            "first_move": False,
            "en_passant_expire": False
        },
    )


def undo_promotion(board, move):
    move["piece_1"] = pc.Pawn(
        move["piece_1"].location, move["piece_1"].colour, True, False
    )

    undo_regular(board, move)


def undo(move, board):
    if move["type"] == "regular":
        undo_regular(board, move)

    elif move["type"] == "castle":
        undo_regular(board, move["king_move"])
        undo_regular(board, move["rook_move"])

    elif move["type"] == "promotion":
        undo_promotion(board, move)

    elif move["type"] == "double_push":
        undo_regular(board, move)
        move["piece_1"].en_passant_able = False

    else:
        undo_en_passant(board, move)

    if move["piece_2"] is not None:
            board.change_piece_num(1, move["piece_2"].colour)


def notation(move, board):
        notation = ""

        if move["type"] == "castle":
            if move["side"]:
                return "0-0"
            else:
                return "0-0-0"

        notation += move["piece_1"].notation
        notation += board.squares[move["location_1"][0]][move["location_1"][1]].name

        if move["piece_2"] is not None:
            notation += "x"
        else:
            notation += "-"

        notation += board.squares[move["location_2"][0]][move["location_2"][1]].name

        if move["type"] == "promotion":
            notation += move["promotion"][0].upper()

        return notation