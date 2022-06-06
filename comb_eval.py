from dataclasses import dataclass
import comb_pieces as pc
import comb_move_undo as mo_un


@dataclass
class History:

    evals: list
    evals_repeat_possible: list
    moves: list

    def fifty_move(self):
        return len(self.evals_repeat_possible) >= 51

    def add_move(self, group, move):
        if move[0] in group.keys():
            group[move[0]].append(move[4:])
        else:
            group[move[0]] = [move[1:3]]

    def is_repeat(self, group):
        for move_group in group.values():
            if len(move_group) == 1 or move_group[0] != move_group[-1]:
                return False

        return True

    def indexes(self, eval):
        indexes = []
        for x in range(len(self.evals)):
            if eval == self.evals[x]:
                indexes.append(x)
        
        return indexes

    def triad_state_repeat(self, i1, i2, i3):
        for start, stop in [(i1, i2), (i2, i3)]:
            moves = self.moves[start:stop]
            group = {}
            for move in moves:
                self.add_move(group, move)

            if not self.is_repeat(group):
                return False

        return True

    def move_based_state_repeat(self, eval):
        indexes = self.indexes(eval)
        for i1 in indexes:
            for i2 in indexes:
                for i3 in indexes:
                    if i1 < i2 and i2 < i3:
                        if self.triad_state_repeat(i1, i2, i3):
                            return True

        return False

    def eval_triple_repeats(self):
        tier_1 = []
        tier_2 = []
        tier_3 = []

        for eval in self.evals_repeat_possible:
            if eval not in tier_1:
                tier_1.append(eval)

            elif eval not in tier_2:
                tier_2.append(eval)

            elif eval not in tier_3:
                tier_3.append(eval)

        return tier_3

    def threefold(self):
        for eval in self.eval_triple_repeats():
            if self.move_based_state_repeat(eval):
                return True

        return False

    def evals_repeat_possible_pull(self):
        self.evals.reverse()
        self.moves.reverse()
        for eval, move in zip(self.evals, self.moves):
            self.evals_repeat_possible.append(eval)
            if move[2] == "-" or "x" in move:
                break

        self.evals.reverse()
        self.moves.reverse()

    def record(self, move, board, eval):
        self.moves.append(mo_un.notation(move, board))
        self.evals.append(eval)
        if (
            move["piece_2"] is not None 
            or type(move["piece_1"]) == pc.Pawn
        ):
            self.evals_repeat_possible.clear()

        self.evals_repeat_possible.append(eval)
        
    def unrecord(self):
        self.evals.pop(-1)
        self.moves.pop(-1)
        self.evals_repeat_possible.pop(-1)
        if len(self.evals_repeat_possible) == 0:
            self.evals_repeat_possible_pull()


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
    if board.white_pieces["king"].location is None:
        return -1000
    elif board.black_pieces["king"].location is None:
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