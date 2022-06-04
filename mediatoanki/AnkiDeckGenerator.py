import os
from typing import List

import genanki

from mediatoanki.deck.flashcard.FlashCardTemplate import FlashCardTemplate
from mediatoanki.model.anki.FlashCardFieldsContent import \
    FlashCardFieldsContent
from mediatoanki.model.Subtitle import Subtitle
from mediatoanki.utils.AnkiUtils import AnkiUtils
from mediatoanki.utils.FileUtils import FileUtils


class AnkiDeckGenerator:
    def __init__(self, destination: str, deck_name: str):
        self._set_destination(destination)
        self._deck_name = deck_name

    def _set_destination(self, destination: str):
        FileUtils.validate_directory(destination)
        self.__destination = destination

    def generate_deck_based_on(self, subtitles: List[Subtitle]):
        model = FlashCardTemplate().model
        deck = genanki.Deck(
            AnkiUtils.generate_deck_id(),
            self._deck_name,
        )

        for sub in subtitles:
            fields_content = FlashCardFieldsContent(sub.subtitle_id, sub.text)
            note = genanki.Note(
                model=model,
                fields=fields_content,
            )
            deck.add_note(note)

        path = os.path.join(self.__destination, f"{self._deck_name}.apkg")
        genanki.Package(deck).write_to_file(path)
