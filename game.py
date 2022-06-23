from dataclasses import dataclass
import board as bd
import branches as br
import engine as eg
import pieces as pc
import move_undo as mo_un
import random

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
class Game:

    engine: eg.Engine
    user_colour: bool

    white_time: int = 0
    black_time: int = 0

    turn: bool = True

    engine_on: bool = True
    lines_on: bool = True

    white_win: bool = False
    black_win: bool = False
    draw: bool = False
    stopped: bool = False


    def concluded(self):
        return self.white_win or self.black_win or self.draw or self.stopped

    def illustrate(self):
        if self.user_colour:
            find_piece = lambda x, y: self.engine.board.squares[y][7 - x].piece
        else:
            find_piece = lambda x, y: self.engine.board.squares[7 - y][x].piece

        for x in range(8):
            row = ""
            for y in range(8):
                if find_piece(x, y) is not None:
                    row += abreviation(find_piece(x, y)) + " "
                else:
                    row += "- "

            print(row)

    def win_lose_draw_update(self):
        win_lose_draw = self.engine.win_lose_draw()

        if win_lose_draw is not None:
            if win_lose_draw > 0:
                self.white_win = True
            
            elif win_lose_draw < 0:
                self.black_win = True

            else:
                self.draw = True

    def move(self, move):
        self.engine.move(move, self.turn)
        self.engine.notebook.journey.clear()
        self.turn = not self.turn

    def user_move(self, user_move):
        options = [option for option in self.engine.branches(self.turn)]
        moves = [mo_un.notation(option, self.engine.board) for option in options]

        for move, option in zip(moves, options):
            if move.lower() == user_move:
                return option

    def user_input(self):
        while not self.concluded():
            user_input = input("User: ").lower()

            if user_input == "engine on":
                self.engine_on = True

            elif user_input == "engine off":
                self.engine_on = False

            elif user_input == "stop":
                self.stopped = True

            elif user_input == "lines on":
                self.lines_on = True

            elif user_input == "lines off":
                self.lines_on = False

            else:
                user_move = self.user_move(user_input)
                if user_move is not None:
                    return user_move
                else:
                    print(
                        "Commands: engine on, engine off, stop, lines on, lines off, stop\n"
                        + "Move format: {piece notation (Empty for pawn) }{piece's square}{- or x for capturing}{target square}\n" 
                        + "   ex) Qd1-d3: Move queen from d1 to d3\n"
                        + "       e6xf5: Pawn on e6 captures piece on f5\n"
                        + "       0-0: castle short\n"
                        + "       0-0-0: castle long\n"
                        + "       h7-h8R: pawn on h7 reaches end rank and promotes to rook\n"
                    )

    def user_turn(self):
        user_move = self.user_input()
        if user_move is not None:
            self.move(user_move)
            self.win_lose_draw_update()

            print("")
            self.illustrate()
            print("")

    def engine_turn(self):
        # self.engine.explore(self.turn)
        self.engine.notebook.top_lines.clear()
        branches = self.engine.branches(self.turn)
        self.engine.search(self.turn, 1, 5, branches)

        p_total = 0
        for line in self.engine.notebook.top_lines:
            p_total += abs(line[0])

        p_rand = random.uniform(0, p_total)
        p = 0
        for line in self.engine.notebook.top_lines:
            p += abs(line[0])
            if p > p_rand:
                engine_move = line[1][0]
                break

        self.move(engine_move)
        self.win_lose_draw_update()
        print(f"Engine: {mo_un.notation(engine_move, self.engine.board)}")

        print("")
        self.illustrate()
        print("")

        if self.lines_on:
            self.engine.top_lines_show(1)
            print("")


def get_input(valid_inputs, input_message):
    user_input = input(input_message).lower()
    while user_input not in valid_inputs:
        print(f"Valid inputs: {valid_inputs}")
        user_input = input(input_message).lower()

    return user_input


def get_colour(user_colour_choice):
    if user_colour_choice == "white":
        return True
    
    elif user_colour_choice == "black":
        return False

    else:
        return random.choice([True, False])


def game_start():
    mode = get_input([
        "regular", 
        "chess 960", 
        "reverse chess", 
        "king of the hill"
    ], "Gamemode: ")
    print("")
    user_colour_choice = get_input(["white", "black", "random"], "User colour: ")

    return Game(eg.engine_setup(mode), get_colour(user_colour_choice))


def game_start_nn():
    return Game(eg.engine_setup("nn"), get_colour("white"))