from dataclasses import dataclass
import moptions as mo
import move_undo as mv


@dataclass
class Piece():
    colour: bool
    location: list
    moptions: list = []
    moved: bool = False
    en_passant_able: bool = False

    def difference_location(self, difference):
        return mo.difference_location(self.location, difference)

    def moptions_location_update(self, board):
        for moption in self.moptions:
            moption.location_update(self.location, board)

    def options(self):
        options = []
        for moption in self.moptions:
            options += moption.options

        return options


@dataclass
class Pawn(Piece):
    value: int = 1
    notation: str = ""

    def setup_moptions(self, board):
        if self.colour:
            advance = self.difference_location([0, 1])
            double_advance = self.difference_location([0, 2])

        else:
            advance = self.difference_location([0, -1])
            double_advance = self.difference_location([0, -2])

        self.moptions = [
            mo.Moption_Regular(
                mv.Move(self.location, None, advance, None),
            ),
            mo.Moption_Double_Push(
                mv.Move(self.location, None, double_advance, None),
            ),
            mo.Moption_En_Passant(
                mv.Compound_Move(
                    mv.Move(self.location, None, self.difference_location([1, 0]), None),
                    mv.Move(self.location, None, advance, None)
                ),
                mv.Compound_Move(
                    mv.Move(self.location, None, self.difference_location([-1, 0]), None),
                    mv.Move(self.location, None, advance, None)
                ),
            )
        ]

        self.moptions_location_update(board)


@dataclass
class Rook(Piece):
    value: int = 5
    notation: str = "R"
    
    def setup_moptions(self, board):
        self.moptions = [
            mo.Moption_Extend(
                [0, 1], None
            ),
            mo.Moption_Extend(
                [1, 0], None
            ),
            mo.Moption_Extend(
                [0, -1], None
            ),
            mo.Moption_Extend(
                [-1, 0], None
            )
        ]

        self.moptions_location_update(board)


@dataclass
class Knight(Piece):
    value: int = 3
    notation: str = "Kn"

    def setup_moptions(self, board):
        self.moptions = [
            mo.Moption_Regular(
                mv.Move(self.location, None, self.difference_location([1, 2]), None),
                mv.Move(self.location, None, self.difference_location([2, 1]), None),
                mv.Move(self.location, None, self.difference_location([2, -1]), None),
                mv.Move(self.location, None, self.difference_location([1, -2]), None),
                mv.Move(self.location, None, self.difference_location([-1, -1]), None),
                mv.Move(self.location, None, self.difference_location([-2, -1]), None),
                mv.Move(self.location, None, self.difference_location([-2, 1]), None),
                mv.Move(self.location, None, self.difference_location([-1, 2]), None)
            )
        ]

        self.moptions_location_update(board)


@dataclass
class Bishop(Piece):
    value: int = 3
    notation: str = "B"

    def setup_moptions(self, board):
        self.moptions = [
            mo.Moption_Extend(
                [1, 1], None
            ),
            mo.Moption_Extend(
                [1, -1], None
            ),
            mo.Moption_Extend(
                [-1, -1], None
            ),
            mo.Moption_Extend(
                [-1, 1], None
            )
        ]

        self.moptions_location_update(board)


@dataclass
class Queen(Piece):
    value: int = 9
    notation: str = "Q"

    def setup_moptions(self, board):
        self.moptions = [
            mo.Moption_Extend(
                [0, 1], None
            ),
            mo.Moption_Extend(
                [1, 0], None
            ),
            mo.Moption_Extend(
                [0, -1], None
            ),
            mo.Moption_Extend(
                [-1, 0], None
            ),
            mo.Moption_Extend(
                [1, 1], None
            ),
            mo.Moption_Extend(
                [1, -1], None
            ),
            mo.Moption_Extend(
                [-1, -1], None
            ),
            mo.Moption_Extend(
                [-1, 1], None
            )
        ]

        self.moptions_location_update(board)


@dataclass
class King(Piece):
    value: int = 2
    notation: str = "K"

    def setup_moptions(self, board):
        self.moptions = [
            mo.Moption_Regular(
                mv.Move(self.location, None, self.difference_location([0, 1]), None),
                mv.Move(self.location, None, self.difference_location([1, 0]), None),
                mv.Move(self.location, None, self.difference_location([0, -1]), None),
                mv.Move(self.location, None, self.difference_location([-1, 0]), None),
                mv.Move(self.location, None, self.difference_location([1, 1]), None),
                mv.Move(self.location, None, self.difference_location([1, -1]), None),
                mv.Move(self.location, None, self.difference_location([-1, -1]), None),
                mv.Move(self.location, None, self.difference_location([-1, 1]), None)
            )
        ]

        self.moptions_location_update(board)
