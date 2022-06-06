from dataclasses import dataclass
import comb_board as bd
import comb_branches as br
import comb_move_undo as mo_un
import comb_pieces as pc
import comb_eval as ev


def abreviation(piece):
    if type(piece) == pc.Pawn:
        abreviation = "P"
    elif type(piece) == pc.Knight:
        abreviation = "N"
    elif type(piece) == pc.Bishop:
        abreviation = "B"
    elif type(piece) == pc.Rook:
        abreviation = "R"
    elif type(piece) == pc.Queen:
        abreviation = "Q"
    else:
        abreviation = "K"

    if piece.colour:
        return abreviation
    else:
        return abreviation.lower()


@dataclass
class Notebook:

    journey: list
    lines: list
    top_lines: list

    def setup_lines(self, depth):
        self.lines = [[] for x in range(depth)]

    def get_eval(self, line):
        return line[0]

    def collect_max_min(self, level, turn):
        self.lines[level].sort(reverse=turn, key=self.get_eval)
        self.lines[level - 1].append(self.lines[level][0])
        self.lines[level].clear()

    def collect_top_lines(self, turn, n, location, lines):
        lines.sort(reverse=turn, key=self.get_eval)

        moves = []
        for line in lines:
            if line[1][0] not in moves:
                moves.append(line[1][0])
                location.append(line)

            if len(moves) == n:
                break

        lines.clear()

    def collect_top_lines_search(self, turn, n):
        self.collect_top_lines(turn, n, self.top_lines, self.lines[0])


@dataclass
class Engine:

    history: ev.History
    notebook: Notebook
    board: bd.Board

    depth: int
    top_lines_filters: list

    material_value: float
    centralization_value: float

    def update_centralization(self, piece):
        piece.centralization = pc.centralization_eval(piece.location)


    def move(self, move):
        mo_un.move(move, self.board)
        self.notebook.journey.append(move)
        self.history.record(move, self.board, self.eval())
        self.update_centralization(move["piece_1"])

    def undo(self):
        move = self.notebook.journey[-1]

        mo_un.undo(move, self.board)
        self.history.unrecord()
        self.notebook.journey.pop(-1)
        self.update_centralization(move["piece_1"])
        if move["piece_2"] is not None:
            self.update_centralization(move["piece_2"])
        
    def mate_eval(self, turn):
        for move in br.regular_branches(self.board, not turn):
            self.move(move)
            win_lose_draw = self.win_lose_draw()
            self.undo()

            if (
                win_lose_draw is not None
                and abs(win_lose_draw) == 1000
            ):
                
                if turn:
                    return -1001
                else:
                    return 1001

        return 0


    def mate_check(self, turn, line):
        if abs(line[0]) == 1000 and len(line[1]) == 3:
            line[0] = self.mate_eval(turn)
            for x in range(2):
                line[1].pop(-1)


    def recursive_search(self, turn, depth, level = 1):
        win_lose_draw = self.win_lose_draw()
        if win_lose_draw is not None:
            self.notebook.lines[level - 1].append(
                [win_lose_draw, [self.notebook.journey[-1]]]
            )

        elif level == depth:
            self.notebook.lines[level - 1].append(
                [self.history.evals[-1], [self.notebook.journey[-1]]]
            )

        else:
            for move in self.branches(turn):
                self.move(move)
                self.recursive_search(not turn, depth, level = level + 1)
                self.undo()

            self.notebook.collect_max_min(level, turn)
            self.notebook.lines[level - 1][-1][1].insert(0, self.notebook.journey[-1])
            self.mate_check(turn, self.notebook.lines[level - 1][-1])


    def search(self, turn, depth, top_lines_num, considered_moves):
        for move in considered_moves:
            self.move(move)
            self.recursive_search(not turn, depth)
            self.undo()

        self.notebook.collect_top_lines_search(
            turn, top_lines_num
        )


    def explore(self, turn):
        moves = self.branches(turn)
        for depth in range(self.depth // 2):
            self.notebook.top_lines.clear()
            self.search(turn, 2 * (depth + 1), round(len(moves) * self.top_lines_filters[depth]), moves)
            moves = [top_line[1][0] for top_line in self.notebook.top_lines]


    def top_lines_show(self, n):
        for line_index in range(n):
            line = self.notebook.top_lines[line_index]
            notation = [
                mo_un.notation(move, self.board)
                for move in line[1]
            ]

            if line[0] == 1001:
                eval = "M"
                eval += f"{len(line[1]) // 2 + len(line[1]) % 2}"
                eval += "_white"

            elif line[0] == -1001:
                eval = "M"
                eval += f"{len(line[1]) // 2 + len(line[1]) % 2}"
                eval += "_black"

            else:
                # based on avg centralization and material value of a piece scaled down
                eval_scale_factor = 0.42 / (
                    0.42 * self.material_value + 0.58 * self.centralization_value
                )
                eval = round(
                    line[0] * eval_scale_factor, 2
                )

            print(eval, notation)

    def illustrate(self, colour):
        if colour:
            find_piece = lambda x, y: self.board.squares[y][7 - x].piece
        else:
            find_piece = lambda x, y: self.board.squares[7 - y][x].piece

        for x in range(8):
            row = ""
            for y in range(8):
                if find_piece(x, y) is not None:
                    row += abreviation(find_piece(x, y)) + " "
                else:
                    row += "- "

            print(row)

    def default_setup(self):
        ev.initialize_centralization(self.board)
        self.history.evals.append(self.eval())
        self.history.evals_repeat_possible.append(self.eval())
        self.notebook.setup_lines(self.depth)
        

@dataclass
class Engine_regular(Engine):

    def branches(self, colour):
        return br.regular_branches(self.board, colour)

    def win_lose_draw(self):
        return ev.regular_win_lose_draw(self.board, self.history)

    def eval(self):
        return ev.regular_eval(self.material_value, self.centralization_value, self.board)

    def setup(self):
        self.board.setup_regular()
        self.default_setup()
        

@dataclass
class Engine_960(Engine):

    def branches(self, colour):
        return br.regular_branches(self.board, colour)

    def win_lose_draw(self):
        return ev.regular_win_lose_draw(self.board, self.history)

    def eval(self):
        return ev.regular_eval(self.material_value, self.centralization_value, self.board)

    def setup(self):
        self.board.setup_960()
        self.default_setup()


@dataclass
class Engine_reverse(Engine):

    def branches(self, colour):
        return br.reverse_branches(self.board, colour)

    def win_lose_draw(self):
        return ev.reverse_win_lose_draw(self.board, self.history)

    def eval(self):
        return -ev.regular_eval(self.material_value, self.centralization_value, self.board)

    def setup(self):
        self.board.setup_regular()
        self.default_setup()


@dataclass
class Engine_koth(Engine):

    def branches(self, colour):
        return br.regular_branches(self.board, colour)

    def win_lose_draw(self):
        return ev.koth_win_lose_draw(self.board, self.history)

    def eval(self):
        return ev.regular_eval(self.material_value, self.centralization_value, self.board)

    def setup(self):
        self.board.setup_regular()
        self.default_setup()


def engine_setup(mode, depth = 4, top_lines_filters = [0.75, 0.25], material_value = 10.0, centralization_value = 1.0):
    if mode == "regular":
        engine = Engine_regular(
            ev.History([], [], []), 
            Notebook([], [], []), 
            bd.Board({}, {}, []), 
            depth, 
            top_lines_filters, 
            material_value, 
            centralization_value
    )
    
    elif mode == "chess 960":
        engine = Engine_960(
            ev.History([], [], []), 
            Notebook([], [], []), 
            bd.Board({}, {}, []), 
            depth, 
            top_lines_filters, 
            material_value, 
            centralization_value
    )
    
    elif mode == "reverse":
        engine = Engine_reverse(
            ev.History([], [], []), 
            Notebook([], [], []), 
            bd.Board({}, {}, []), 
            depth, 
            top_lines_filters, 
            material_value, 
            centralization_value
    )
    
    elif mode == "king of the hill":
        engine = Engine_koth(
            ev.History([], [], []), 
            Notebook([], [], []), 
            bd.Board({}, {}, []), 
            depth, 
            top_lines_filters, 
            material_value, 
            centralization_value
    )

    engine.setup()

    return engine