import random


class AnkiUtils:
    @staticmethod
    def generate_deck_id() -> int:
        return random.randrange(1 << 30, 1 << 31)
