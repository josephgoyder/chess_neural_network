from dataclasses import dataclass
import comb_pieces as pc
import random as rd


@dataclass
class Square:

    piece: pc.Piece
    name: str

    def full(self):
        return self.piece is not None


@dataclass
class Board:

    white_pieces: dict
    black_pieces: dict

    squares: list

    white_piece_num: int = 0
    black_piece_num: int = 0

    def pieces(self, colour):
        if colour:
            return self.white_pieces

        return self.black_pieces

    def piece_num(self, colour):
        if colour:
            return self.white_piece_num

        return self.black_piece_num

    def change_piece_num(self, value, colour):
        if colour:
            self.white_piece_num += value

        else:
            self.black_piece_num += value

    def setup(self, white_pieces, black_pieces):
        self.white_pieces = white_pieces
        self.black_pieces = black_pieces

        self.squares = [
            [
                Square(None, "a1"), 
                Square(None, "a2"), 
                Square(None, "a3"), 
                Square(None, "a4"), 
                Square(None, "a5"), 
                Square(None, "a6"), 
                Square(None, "a7"), 
                Square(None, "a8")
            ],
            [
                Square(None, "b1"), 
                Square(None, "b2"), 
                Square(None, "b3"), 
                Square(None, "b4"), 
                Square(None, "b5"), 
                Square(None, "b6"), 
                Square(None, "b7"), 
                Square(None, "b8")
            ],
            [
                Square(None, "c1"), 
                Square(None, "c2"), 
                Square(None, "c3"), 
                Square(None, "c4"), 
                Square(None, "c5"), 
                Square(None, "c6"), 
                Square(None, "c7"), 
                Square(None, "c8")
            ],
            [
                Square(None, "d1"), 
                Square(None, "d2"), 
                Square(None, "d3"), 
                Square(None, "d4"), 
                Square(None, "d5"), 
                Square(None, "d6"), 
                Square(None, "d7"), 
                Square(None, "d8")
            ],
            [
                Square(None, "e1"), 
                Square(None, "e2"), 
                Square(None, "e3"), 
                Square(None, "e4"), 
                Square(None, "e5"), 
                Square(None, "e6"), 
                Square(None, "e7"), 
                Square(None, "e8")
            ],
            [
                Square(None, "f1"), 
                Square(None, "f2"), 
                Square(None, "f3"), 
                Square(None, "f4"), 
                Square(None, "f5"), 
                Square(None, "f6"), 
                Square(None, "f7"), 
                Square(None, "f8")
            ],
            [
                Square(None, "g1"), 
                Square(None, "g2"), 
                Square(None, "g3"), 
                Square(None, "g4"), 
                Square(None, "g5"), 
                Square(None, "g6"), 
                Square(None, "g7"), 
                Square(None, "g8")
            ],
            [
                Square(None, "h1"), 
                Square(None, "h2"), 
                Square(None, "h3"), 
                Square(None, "h4"), 
                Square(None, "h5"), 
                Square(None, "h6"), 
                Square(None, "h7"), 
                Square(None, "h8")
            ]
        ]

        for colour in [True, False]:
            for piece in self.pieces(colour).values():
                if piece.location is not None:
                    self.squares[piece.location[0]][piece.location[1]].piece = piece
                    self.change_piece_num(1, colour)

    def setup_regular(self):
        white_pieces = {
            "pawn_1": pc.Pawn([0, 1], True),
            "pawn_2": pc.Pawn([1, 1], True),
            "pawn_3": pc.Pawn([2, 1], True),
            "pawn_4": pc.Pawn([3, 1], True),
            "pawn_5": pc.Pawn([4, 1], True),
            "pawn_6": pc.Pawn([5, 1], True),
            "pawn_7": pc.Pawn([6, 1], True),
            "pawn_8": pc.Pawn([7, 1], True),
            "rook_1": pc.Rook([7, 0], True),
            "rook_2": pc.Rook([0, 0], True),
            "knight_1": pc.Knight([6, 0], True),
            "knight_2": pc.Knight([1, 0], True),
            "bishop_1": pc.Bishop([5, 0], True),
            "bishop_2": pc.Bishop([2, 0], True),
            "queen": pc.Queen([3, 0], True),
            "king": pc.King([4, 0], True),
        }

        black_pieces = {
            "pawn_1": pc.Pawn([0, 6], False),
            "pawn_2": pc.Pawn([1, 6], False),
            "pawn_3": pc.Pawn([2, 6], False),
            "pawn_4": pc.Pawn([3, 6], False),
            "pawn_5": pc.Pawn([4, 6], False),
            "pawn_6": pc.Pawn([5, 6], False),
            "pawn_7": pc.Pawn([6, 6], False),
            "pawn_8": pc.Pawn([7, 6], False),
            "rook_1": pc.Rook([7, 7], False),
            "rook_2": pc.Rook([0, 7], False),
            "knight_1": pc.Knight([6, 7], False),
            "knight_2": pc.Knight([1, 7], False),
            "bishop_1": pc.Bishop([5, 7], False),
            "bishop_2": pc.Bishop([2, 7], False),
            "queen": pc.Queen([3, 7], False),
            "king": pc.King([4, 7], False)
        }

        self.setup(white_pieces, black_pieces)

    def assign_location(self, avaliable):
        choice = rd.choice(avaliable)
        avaliable.remove(choice)

        return choice

    def setup_960(self):
        locations = [0, 0, 0, 0, 0, 0, 0, 0]

        avaliable = [0, 1, 2, 3, 4, 5, 6, 7]

        dark_square_bishop_choice = rd.randint(0, 3) * 2
        locations[2] = dark_square_bishop_choice
        avaliable.remove(dark_square_bishop_choice)

        light_square_bishop_choice = rd.randint(0, 3) * 2 + 1
        locations[5] = light_square_bishop_choice
        avaliable.remove(light_square_bishop_choice)

        rooks_king = [0, 0, 0]
        for x in range(3):
            rooks_king[x] = self.assign_location(avaliable)

        rooks_king.sort()
        locations[0] = rooks_king[0]
        locations[4] = rooks_king[1]
        locations[7] = rooks_king[2]

        for x in [1, 3, 6]:
            locations[x] = self.assign_location(avaliable)

        white_pieces = {
            "pawn_1": pc.Pawn([0, 1], True),
            "pawn_2": pc.Pawn([1, 1], True),
            "pawn_3": pc.Pawn([2, 1], True),
            "pawn_4": pc.Pawn([3, 1], True),
            "pawn_5": pc.Pawn([4, 1], True),
            "pawn_6": pc.Pawn([5, 1], True),
            "pawn_7": pc.Pawn([6, 1], True),
            "pawn_8": pc.Pawn([7, 1], True),
            "rook_1": pc.Rook([locations[7], 0], True),
            "rook_2": pc.Rook([locations[0], 0], True),
            "knight_1": pc.Knight([locations[6], 0], True),
            "knight_2": pc.Knight([locations[1], 0], True),
            "bishop_1": pc.Bishop([locations[5], 0], True),
            "bishop_2": pc.Bishop([locations[2], 0], True),
            "queen": pc.Queen([locations[3], 0], True),
            "king": pc.King([locations[4], 0], True),
        }

        black_pieces = {
            "pawn_1": pc.Pawn([0, 6], False),
            "pawn_2": pc.Pawn([1, 6], False),
            "pawn_3": pc.Pawn([2, 6], False),
            "pawn_4": pc.Pawn([3, 6], False),
            "pawn_5": pc.Pawn([4, 6], False),
            "pawn_6": pc.Pawn([5, 6], False),
            "pawn_7": pc.Pawn([6, 6], False),
            "pawn_8": pc.Pawn([7, 6], False),
            "rook_1": pc.Rook([locations[7], 7], False),
            "rook_2": pc.Rook([locations[0], 7], False),
            "knight_1": pc.Knight([locations[6], 7], False),
            "knight_2": pc.Knight([locations[1], 7], False),
            "bishop_1": pc.Bishop([locations[5], 7], False),
            "bishop_2": pc.Bishop([locations[2], 7], False),
            "queen": pc.Queen([locations[3], 7], False),
            "king": pc.King([locations[4], 7], False)
        }

        self.setup(white_pieces, black_pieces)
        