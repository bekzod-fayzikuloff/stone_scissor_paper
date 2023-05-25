import hashlib
import hmac
import random


class Sign:
    def __init__(self, moves: list[str]) -> None:
        self._moves = moves
        self._chosen = random.choice(self._moves)
        self._hmac_key = hashlib.sha256(random.randbytes(1)).hexdigest()

    def change_sign(self) -> None:
        self._chosen = random.choice(self._moves)
        self._hmac_key = hashlib.sha256(random.randbytes(1)).hexdigest()

    @property
    def chosen(self) -> str:
        return self._chosen

    @property
    def hmac(self) -> str:
        return hmac.new(
            key=self.hmac_key.encode(), msg=self.chosen.encode(), digestmod=hashlib.sha256
        ).hexdigest()

    @property
    def hmac_key(self) -> str:
        return self._hmac_key

    @staticmethod
    def ct_compare(sign_1, sign_2) -> bool:
        if len(sign_1) != len(sign_2):
            return False

        result = 0
        for ch_a, ch_b in zip(sign_1, sign_2):
            result |= ord(ch_a) ^ ord(ch_b)
        return result == 0
