from dataclasses import dataclass

@dataclass
class Piece:

    location: list
    colour: bool
    captured: bool = False
    centralization: int = 0

    def on_board(self, location_x, location_y):
        return 0 <= location_x <= 7 and 0 <= location_y <= 7

    def regular_add(self, direction, output, squares):
        location = [self.location[0] + direction[0], self.location[1] + direction[1]]

        if self.on_board(location[0], location[1]) and not self.captured:
            square = squares[location[0]][location[1]]

            if not square.full() or square.piece.colour != self.colour:
                output.append({"location_2": location, "type": "regular"})

            else:
                output.append(0)

        else:
            output.append(0)

    def regular_extend(self, direction, output, squares):
        extention = [0] * 7

        if not self.captured:
            location = [self.location[0] + direction[0], self.location[1] + direction[1]]
            distance = 0

            while self.on_board(location[0], location[1]):
                square = squares[location[0]][location[1]]

                if square.full():
                    if square.piece.colour == self.colour:
                        break
                    else:
                        extention[distance] = {"location_2": list(location), "type": "regular"}
                        break
                else:
                    extention[distance] = {"location_2": list(location), "type": "regular"}

                    location[0] += direction[0]
                    location[1] += direction[1]
                    distance += 1

        output += extention

    def regular(self, options, squares, function):
        output = []

        for option in options:
            function(option, output, squares)

        return output


@dataclass
class Pawn(Piece):

    en_passant_able: bool = False
    moved: bool = False
    value: int = 1
    notation: str = ""

    def promotion_output(self, squares, output, location):
        for promotion in ["queen", "knight", "bishop", "rook"]:
            output.append(
                {"location_2": location, "type": "promotion", "promotion": promotion}
            )

    def promotion_capture_push(self, squares, output, location):
        if self.colour and self.location[1] == 6:
            self.promotion_output(squares, output, location)

        elif not self.colour and self.location[1] == 1:
            self.promotion_output(squares, output, location)

        else:
            output.append({"location_2": location, "type": "regular"})

    def double_push(self, squares, output, colour_mult):
        if not squares[self.location[0]][self.location[1] + colour_mult * 2].full():
            if not squares[self.location[0]][self.location[1] + colour_mult].full():
                output.append(
                    {
                        "location_2": [
                            self.location[0],
                            self.location[1] + 2 * colour_mult,
                        ],
                        "type": "double_push",
                    }
                )
            else:
                output.append(0)

        else:
            output.append(0)

    def en_passant(self, squares, output, location):
        square = squares[location[0]][self.location[1]]
        if (
            square.full()
            and type(square.piece) == Pawn
            and square.piece.en_passant_able
            and square.piece.colour != self.colour
        ):
            output.append(
                {
                    "location_3": location,
                    "location_2": [location[0], self.location[1]],
                    "type": "en_passant",
                }
            )

        else:
            output.append(0)

    def options_generic_pawn(self, squares, output, colour_mult):
        if self.on_board(self.location[0], self.location[1] + colour_mult) and not self.captured:
            if not self.moved:
                self.double_push(squares, output, colour_mult)
            
            else:
                output.append(0)

            if not squares[self.location[0]][self.location[1] + colour_mult].full():
                self.promotion_capture_push(
                    squares, output, [self.location[0], self.location[1] + colour_mult]
                )

            else:
                output += [0]*4

        else:
            output += [0]*5

        for side_mult in [1, -1]:

            if (
            self.on_board(self.location[0] + side_mult, self.location[1] + colour_mult) 
            and not self.captured
            ):
                square = squares[self.location[0] + side_mult][
                    self.location[1] + colour_mult
                ]

                if square.full() and square.piece.colour != self.colour:
                    self.promotion_capture_push(
                        squares,
                        output,
                        [self.location[0] + side_mult, self.location[1] + colour_mult],
                    )

                else:
                    output.append(0)

                self.en_passant(
                    squares,
                    output,
                    [self.location[0] + side_mult, self.location[1] + colour_mult],
                )

            else:
                output += [0] * 2
                

    def options(self, squares):
        output = []

        if self.colour:
            colour_mult = 1
        else:
            colour_mult = -1

        self.options_generic_pawn(squares, output, colour_mult)

        return output


@dataclass
class Rook(Piece):

    moved: bool = False
    value: int = 5
    notation: str = "R"

    def options(self, squares):
        return self.regular(
            [(0, 1), (1, 0), (0, -1), (-1, 0)], squares, self.regular_extend
        )


@dataclass
class Knight(Piece):

    moved: bool = False
    value: int = 3
    notation: str = "Kn"

    def options(self, squares):
        return self.regular(
            [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)],
            squares,
            self.regular_add,
        )


@dataclass
class Bishop(Piece):

    moved: bool = False
    value: int = 3
    notation: str = "B"

    def options(self, squares):
        return self.regular(
            [(1, 1), (1, -1), (-1, -1), (-1, 1)], squares, self.regular_extend
        )


@dataclass
class Queen(Piece):

    moved: bool = False
    value: int = 9
    notation: str = "Q"

    def options(self, squares):
        return self.regular(
            [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
            squares,
            self.regular_extend,
        )


@dataclass
class King(Piece):

    moved: bool = False
    value: int = 2
    notation: str = "K"

    def options(self, squares):
        return self.regular(
            [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
            squares,
            self.regular_add,
        )

def centralization_eval(location):
    return 7 - abs(location[0] - 3.5) - abs(location[1] - 3.5)