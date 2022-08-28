import os.path
from typing import List, Type

from genanki import Deck, Note, Package

from mediatoanki.deck.DeckGenerator import DeckGenerator
from mediatoanki.deck.flashcard.FlashCardTemplate import FlashCardTemplate
from mediatoanki.model.anki.FlashCardFieldsContent import \
    FlashCardFieldsContent
from mediatoanki.model.file.Subtitle import Subtitle
from mediatoanki.utils.AnkiUtils import AnkiUtils


class AnkiDeckGenerator(DeckGenerator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_deck(
            self,
            name: str
    ) -> Deck:
        return Deck(
            AnkiUtils.generate_deck_id(),
            name
        )

    def create_notes(
            self,
            subtitles: List[Subtitle],
            template: FlashCardTemplate,
            fields_content: Type[FlashCardFieldsContent]
    ) -> List[Note]:
        notes = []
        for subtitle in subtitles:
            fields = fields_content(
                subtitle.id, subtitle.text
            )
            note = Note(
                model=template.model,
                fields=fields.html,
            )
            notes.append(note)

        return notes

    def append_notes_in_deck(self, deck: Deck, notes: List[Note]):
        for note in notes:
            deck.add_note(note)

    def save_deck(self, deck: Deck, destination: str):
        super().save_deck(deck, destination)
        deck_path = os.path.join(destination, f"{deck.name}.apkg")
        Package(deck).write_to_file(deck_path)
