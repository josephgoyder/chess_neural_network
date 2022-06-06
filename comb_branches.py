import comb_pieces as pc


def can_castle(squares, king, rook):
    if king.moved or king.location is None:
        return False
    if rook.moved or rook.location is None:
        return False

    castling_range = [king.location[0], rook.location[0]]
    castling_range.sort()

    castling_squares = [
        [x, king.location[1]] for x in range(castling_range[0] + 1, castling_range[1])
    ]

    for location in castling_squares:
        if squares[location[0]][location[1]].full():
            return False

    return True


def generate_castle_move(king, rook, king_location_2, rook_location_2, side):
    return {
        "piece_1": king,
        "piece_2": None,
        "side": side,
        "type": "castle",
        "king_move": {
            "piece_1": king,
            "piece_2": None,
            "location_1": king.location,
            "location_2": king_location_2,
            "type": "regular",
            "first_move": True,
            "en_passant_expire": False
        },
        "rook_move": {
            "piece_1": rook,
            "piece_2": None,
            "location_1": rook.location,
            "location_2": rook_location_2,
            "type": "regular",
            "first_move": True,
            "en_passant_expire": False
        },
    }


def castle(board, colour, side):
    if colour:
        if side:
            if can_castle(
                board.squares, board.white_pieces["king"], board.white_pieces["rook_1"]
            ):
                return generate_castle_move(
                    board.white_pieces["king"],
                    board.white_pieces["rook_1"],
                    [6, 0],
                    [5, 0],
                    True,
                )

        else:
            if can_castle(
                board.squares, board.white_pieces["king"], board.white_pieces["rook_2"]
            ):
                return generate_castle_move(
                    board.white_pieces["king"],
                    board.white_pieces["rook_2"],
                    [2, 0],
                    [3, 0],
                    False,
                )

    else:
        if side:
            if can_castle(
                board.squares, board.black_pieces["king"], board.black_pieces["rook_1"]
            ):
                return generate_castle_move(
                    board.black_pieces["king"],
                    board.black_pieces["rook_1"],
                    [6, 7],
                    [5, 7],
                    True,
                )

        else:
            if can_castle(
                board.squares, board.black_pieces["king"], board.black_pieces["rook_2"]
            ):
                return generate_castle_move(
                    board.black_pieces["king"],
                    board.black_pieces["rook_2"],
                    [6, 7],
                    [5, 7],
                    False,
                )


def add_to_branches(board, branches, piece, option):
    option["location_1"] = piece.location
    option["piece_1"] = piece
    option["piece_2"] = board.squares[option["location_2"][0]][
        option["location_2"][1]
    ].piece

    if not option["piece_1"].moved:
        option["first_move"] = True
    else:
        option["first_move"] = False

    if (
        type(option["piece_1"]) == pc.Pawn 
        and option["piece_1"].en_passant_able
    ):
        option["en_passant_expire"] = True
    else:
        option["en_passant_expire"] = False

    branches.append(option)


def reverse_branches(board, colour):
    branches = []

    captures = False

    for piece in board.pieces(colour).values():
        if piece.location is not None:
            for option in piece.options(board.squares):

                is_capture = (
                    board.squares[option["location_2"][0]][
                        option["location_2"][1]
                    ].piece
                    is not None
                )

                if captures:
                    if is_capture:
                        add_to_branches(board, branches, piece, option)

                elif is_capture:

                    captures = True
                    branches.clear()

                    add_to_branches(board, branches, piece, option)

                else:
                    add_to_branches(board, branches, piece, option)

    if not captures:
        for side in [True, False]:
            _castle = castle(board, colour, side)
            if _castle is not None:
                branches.append(_castle)

    return branches


def regular_branches(board, colour):
    branches = []

    for piece in board.pieces(colour).values():
        if piece.location is not None:
            for option in piece.options(board.squares):
                add_to_branches(board, branches, piece, option)

    for side in [True, False]:
        _castle = castle(board, colour, side)
        if _castle is not None:
            branches.append(_castle)

    return branches