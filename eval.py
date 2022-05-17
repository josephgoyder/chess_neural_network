from dataclasses import dataclass
import pieces as pc
import move_undo as mo_un


@dataclass
class History:

    states: list
    states_repeat_possible: list
    moves: list

    def fifty_move(self):
        return len(self.states_repeat_possible) >= 51

    def threefold(self):
        for state in self.states_repeat_possible:
            if self.states_repeat_possible.count(state) >= 3:
                return True

        return False

    def states_repeat_possible_pull(self):
        self.moves.reverse()
        self.states.reverse()

        for i in range(len(self.moves)):
            self.states_repeat_possible.insert(0, self.states[i])
            if "x" in self.moves[i] or self.moves[i][0] not in ["R", "K", "B", "Q"]:
                break

        self.moves.reverse()
        self.states.reverse()

    def location_sort_criteria(self, location):
        if location is not None:
            return location[0] * 8 + location[1]
        else:
            return -1

    def state(self, board):
        state = {
            "white_rooks": [
                board.white_pieces["rook_1"].location,
                board.white_pieces["rook_2"].location,
            ],
            "white_knights": [
                board.white_pieces["knight_1"].location,
                board.white_pieces["knight_2"].location,
            ],
            "white_bishops": [
                board.white_pieces["bishop_1"].location,
                board.white_pieces["bishop_2"].location,
            ],
            "white_queen": [board.white_pieces["queen"].location],
            "white_king": [board.white_pieces["king"].location],
            "black_rooks": [
                board.black_pieces["rook_1"].location,
                board.black_pieces["rook_2"].location,
            ],
            "black_knights": [
                board.black_pieces["knight_1"].location,
                board.black_pieces["knight_2"].location,
            ],
            "black_bishops": [
                board.black_pieces["bishop_1"].location,
                board.black_pieces["bishop_2"].location,
            ],
            "black_queen": [board.black_pieces["queen"].location],
            "black_king": [board.black_pieces["king"].location],
        }

        for locations in state.values():
            if len(locations) > 1:
                locations.sort(key = self.location_sort_criteria)

        return state

    def initialize_state(self, board):
        state = self.state(board)
        self.states.append(state)
        self.states_repeat_possible.append(state)

    def record(self, move, board):
        if move["piece_2"] is not None:
            board.change_piece_num(-1, move["piece_2"].colour)
            self.states_repeat_possible.clear()

        elif type(move["piece_1"]) == pc.Pawn:
            self.states_repeat_possible.clear()

        self.moves.append(mo_un.notation(move, board))
        state = self.state(board)
        self.states.append(state)
        self.states_repeat_possible.append(state)

    def unrecord(self, move, board):
        if move["piece_2"] is not None:
            board.change_piece_num(1, move["piece_2"].colour)

        self.states_repeat_possible.pop(-1)

        if len(self.states_repeat_possible) == 0:
            self.states_repeat_possible_pull()

        self.states.pop(-1)
        self.moves.pop(-1)


def initialize_centralization(board):
    for pieces in [board.white_pieces.values(), board.black_pieces.values()]:
        for piece in pieces:
            if piece.location is not None:
                piece.centralization = pc.centralization_eval(piece.location)


def regular_eval(material_value, centralization_value, board):
    material = 0
    centralization = 0
    for piece in board.white_pieces.values():
        if piece.location is not None:
            material += piece.value 
            centralization += piece.centralization

    for piece in board.black_pieces.values():
        if piece.location is not None:
            material -=  piece.value 
            centralization -= piece.centralization

    return material * material_value + centralization * centralization_value


def reverse_win_lose_draw(board, history):
    if board.white_piece_num == 0:
        return 1001
    elif board.black_piece_num == 0:
        return -1001

    if history.fifty_move() or history.threefold():
        return 0


def insufficient_material(board):
    for colour in [True, False]:
        if board.piece_num(colour) > 2:
            return False

        for piece in board.pieces(colour).values():
            if piece.location is not None:
                if (
                    type(piece) == pc.Pawn
                    or type(piece) == pc.Rook
                    or type(piece) == pc.Queen
                ):
                    return False

    return True


def regular_win_lose_draw(board, history):
    if board.white_pieces["king"].captured:
        return -1000
    elif board.black_pieces["king"].captured:
        return 1000

    if (
        history.fifty_move()
        or history.threefold()
        or insufficient_material(board)
    ):
        return 0


def koth_win_lose_draw(board, history):
    if (
        board.white_pieces["king"].location is not None
        and board.white_pieces["king"].location[0] >= 3
        and board.white_pieces["king"].location[0] <= 4
        and board.white_pieces["king"].location[1] >= 3
        and board.white_pieces["king"].location[1] <= 4
    ):
        return 1001
    elif (
        board.black_pieces["king"].location is not None
        and board.black_pieces["king"].location[0] >= 3
        and board.black_pieces["king"].location[0] <= 4
        and board.black_pieces["king"].location[1] >= 3
        and board.black_pieces["king"].location[1] <= 4
    ):
        return -1001

    else:
        return regular_win_lose_draw(board, history)


@dataclass
class History:

    states: list
    states_repeat_possible: list
    moves: list

    def fifty_move(self):
        return len(self.states_repeat_possible) >= 51

    def threefold(self):
        for state in self.states_repeat_possible:
            if self.states_repeat_possible.count(state) >= 3:
                return True

        return False

    def states_repeat_possible_pull(self):
        self.moves.reverse()
        self.states.reverse()

        for i in range(len(self.moves)):
            self.states_repeat_possible.insert(0, self.states[i])
            if "x" in self.moves[i] or self.moves[i][0] not in ["R", "K", "B", "Q"]:
                break

        self.moves.reverse()
        self.states.reverse()

    def location_sort_criteria(self, location):
        if location is not None:
            return location[0] * 8 + location[1]
        else:
            return -1

    def state(self, board):
        state = {
            "white_rooks": [
                board.white_pieces["rook_1"].location,
                board.white_pieces["rook_2"].location,
            ],
            "white_knights": [
                board.white_pieces["knight_1"].location,
                board.white_pieces["knight_2"].location,
            ],
            "white_bishops": [
                board.white_pieces["bishop_1"].location,
                board.white_pieces["bishop_2"].location,
            ],
            "white_queen": [board.white_pieces["queen"].location],
            "white_king": [board.white_pieces["king"].location],
            "black_rooks": [
                board.black_pieces["rook_1"].location,
                board.black_pieces["rook_2"].location,
            ],
            "black_knights": [
                board.black_pieces["knight_1"].location,
                board.black_pieces["knight_2"].location,
            ],
            "black_bishops": [
                board.black_pieces["bishop_1"].location,
                board.black_pieces["bishop_2"].location,
            ],
            "black_queen": [board.black_pieces["queen"].location],
            "black_king": [board.black_pieces["king"].location],
        }

        for locations in state.values():
            if len(locations) > 1:
                locations.sort(key = self.location_sort_criteria)

        return state

    def initialize_state(self, board):
        state = self.state(board)
        self.states.append(state)
        self.states_repeat_possible.append(state)

    def record(self, move, board):
        if move["piece_2"] is not None:
            board.change_piece_num(-1, move["piece_2"].colour)
            self.states_repeat_possible.clear()

        elif type(move["piece_1"]) == pc.Pawn:
            self.states_repeat_possible.clear()

        self.moves.append(mo_un.notation(move, board))
        state = self.state(board)
        self.states.append(state)
        self.states_repeat_possible.append(state)

    def unrecord(self, move, board):
        if move["piece_2"] is not None:
            board.change_piece_num(1, move["piece_2"].colour)

        self.states_repeat_possible.pop(-1)

        if len(self.states_repeat_possible) == 0:
            self.states_repeat_possible_pull()

        self.states.pop(-1)
        self.moves.pop(-1)
