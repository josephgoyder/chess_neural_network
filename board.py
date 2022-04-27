from dataclasses import dataclass
from dataclasses import field
import pieces as pc
import random as rd


@dataclass
class Square:

    name: str
    piece: pc.Piece = None

    def full(self):
        return self.piece is not None


@dataclass
class Board:

    white_pieces: dict = field(default_factory=dict)
    black_pieces: dict = field(default_factory=dict)

    squares: list = field(default_factory=list)

    white_piece_num: int = 0
    black_piece_num: int = 0

    def square(self, location):
        if location is not None:
            return self.squares[location[0]][location[1]]

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
                Square("a1"), 
                Square("a2"), 
                Square("a3"), 
                Square("a4"), 
                Square("a5"), 
                Square("a6"), 
                Square("a7"), 
                Square("a8")
            ],
            [
                Square("b1"), 
                Square("b2"), 
                Square("b3"), 
                Square("b4"), 
                Square("b5"), 
                Square("b6"), 
                Square("b7"), 
                Square("b8")
            ],
            [
                Square("c1"), 
                Square("c2"), 
                Square("c3"), 
                Square("c4"), 
                Square("c5"), 
                Square("c6"), 
                Square("c7"), 
                Square("c8")
            ],
            [
                Square("d1"), 
                Square("d2"), 
                Square("d3"), 
                Square("d4"), 
                Square("d5"), 
                Square("d6"), 
                Square("d7"), 
                Square("d8")
            ],
            [
                Square("e1"), 
                Square("e2"), 
                Square("e3"), 
                Square("e4"), 
                Square("e5"), 
                Square("e6"), 
                Square("e7"), 
                Square("e8")
            ],
            [
                Square("f1"), 
                Square("f2"), 
                Square("f3"), 
                Square("f4"), 
                Square("f5"), 
                Square("f6"), 
                Square("f7"), 
                Square("f8")
            ],
            [
                Square("g1"), 
                Square("g2"), 
                Square("g3"), 
                Square("g4"), 
                Square("g5"), 
                Square("g6"), 
                Square("g7"), 
                Square("g8")
            ],
            [
                Square("h1"), 
                Square("h2"), 
                Square("h3"), 
                Square("h4"), 
                Square("h5"), 
                Square("h6"), 
                Square("h7"), 
                Square("h8")
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
        