from itertools import product

from prettytable import PrettyTable

from sign import Sign
from validator import Validator


class Game:
    def __init__(self, moves: list[str]) -> None:
        self._checker = Validator(moves)
        self.moves = self._checker.validate("moves")
        self._sign = Sign(self.moves)

    def start(self) -> None:
        is_valid, *_ = self.moves
        if is_valid:
            self._launch_screen()

    def _launch_screen(self) -> None:
        print(f"HMAC: {self._sign.hmac}")
        print("Available moves:")
        for move_id, move in enumerate(self.moves):
            print(f"{move_id + 1} - {move}")
        print("0 - exit\n? - help")
        self._game_engine()

    def _game_engine(self) -> None:
        while True:
            user_move = self._checker.validate("user_move", input("Enter your move: ").strip())
            if not user_move:
                print("\nSelect a value from the list of available moves!\n")
            elif user_move == "quit":
                print("Thank you, see you soon!")
                break
            elif user_move == "?":
                Table(self.moves).render()
            else:
                print(f"Your move: {self.moves[user_move - 1]}")
                print(f"Computer move: {self._sign.chosen}")
                print(Rules.outcome(self._sign.chosen, self.moves[user_move - 1], self.moves))
                print(f"HMAC KEY: {self._sign.hmac_key}")
                self._sign.change_sign()


class Rules:
    @staticmethod
    def outcome(pc_move: str, user_move: str, available_moves: list[str]) -> str:
        pc_move_index = available_moves.index(pc_move)
        user_move = available_moves.index(user_move)
        if pc_move_index == user_move:
            return "Draw"
        elif user_move > pc_move_index:
            if user_move - pc_move_index <= len(available_moves) // 2:
                return "You lose!"
            return "You win!"
        elif pc_move_index - user_move <= len(available_moves) // 2:
            return "You win"
        return "You lose!"


class Table:
    def __init__(self, moves: list[str]) -> None:
        self.moves = moves

    def render(self) -> None:
        combinations = product(self.moves, self.moves)
        moves_table = PrettyTable()
        moves_table.field_names = ["PC move", "User Move", "User Outcome"]
        for pc_move, user_move in combinations:
            moves_table.add_row([pc_move, user_move, Rules.outcome(pc_move, user_move, self.moves)])
        print(moves_table)
