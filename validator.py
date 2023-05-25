class Validator:
    def __init__(self, moves: list[str]) -> None:
        self.moves = moves

    def validate(self, validator_type: str, *args, **kwargs):
        return getattr(self, f"_validate_{validator_type}")(*args, **kwargs)

    def _validate_moves(self):
        if not self.moves:  # check if the arguments have been passed
            print("Should have any moves")
            return False, 1
        elif len(self.moves) < 3 or not len(self.moves) % 2:  # check for the number and parity of the passed arguments
            print("Moves should be more than 2 and be ord")
            return False, 1
        elif len(list(set(self.moves))) != len(self.moves):  # check for duplicates
            print("The steps should not be repeated")
            return False, 1
        return self.moves

    def _validate_user_move(self, user_move):
        if user_move == "0":
            return "quit"
        elif user_move == "?":
            return "?"
        elif user_move.isdigit() and int(user_move) <= len(self.moves):
            return int(user_move)
        return False
