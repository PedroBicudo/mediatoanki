import os
import random
from typing import List

import genanki

from mediatoanki.model.MediaToAnkiTemplate import MediaToAnkiTemplate
from mediatoanki.model.Subtitle import Subtitle


class AnkiDeckGenerator:
    def __init__(self, destination: str, deck_name: str):
        self._set_destination(destination)
        self._deck_name = deck_name

    def _set_destination(self, destination: str):
        if not AnkiDeckGenerator._is_destination_valid(destination):
            raise

        self.__destination = destination

    @staticmethod
    def _is_destination_valid(destination: str) -> bool:
        return os.path.exists(destination) and os.path.isdir(destination)

    def generate_deck_based_on(self, subtitles: List[Subtitle]):
        model = MediaToAnkiTemplate().model
        deck = genanki.Deck(
            AnkiDeckGenerator._get_random_deck_id(),
            self._deck_name,
        )

        for sub in subtitles:
            note = genanki.Note(
                model=model,
                fields=AnkiDeckGenerator._get_fields_from_sub(sub),
            )
            deck.add_note(note)

        path = os.path.join(self.__destination, f"{self._deck_name}.apkg")
        genanki.Package(deck).write_to_file(path)

    @staticmethod
    def _get_fields_from_sub(subtitle: Subtitle) -> List[str]:
        return [
            f"{subtitle.subtitle_id}",
            f"[sound:{subtitle.subtitle_id}.mp3]",
            f"<img src=\"{subtitle.subtitle_id}.png\">",
            f"{subtitle.text}"
            "", "", "", "", ""
        ]

    @staticmethod
    def _get_random_deck_id() -> int:
        return random.randrange(1 << 30, 1 << 31)
