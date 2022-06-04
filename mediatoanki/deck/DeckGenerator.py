import abc
from typing import List, Type

from genanki import Deck, Note

from mediatoanki.deck.flashcard.FlashCardTemplate import FlashCardTemplate
from mediatoanki.model.anki.FlashCardFieldsContent import \
    FlashCardFieldsContent
from mediatoanki.model.Subtitle import Subtitle
from mediatoanki.utils.FileUtils import FileUtils


class DeckGenerator(object):

    def __init__(
            self,
            deck_name: str,
            note_template: FlashCardTemplate,
            fields_content: Type[FlashCardFieldsContent],
            subtitles: List[Subtitle],
            destination: str
    ):
        FileUtils.validate_directory(destination)
        self.deck_name = deck_name
        self.note_template = note_template
        self.fields_content = fields_content
        self.subtitles = subtitles
        self.destination = destination

    def generate_deck_file_with_notes(self):
        deck = self.create_deck(
            self.deck_name
        )
        notes = self.create_notes(
            self.subtitles, self.note_template, self.fields_content
        )
        self.append_notes_in_deck(deck, notes)
        self.save_deck(deck, self.destination)

    @abc.abstractmethod
    def create_deck(
            self,
            name: str
    ) -> Deck:
        pass

    @abc.abstractmethod
    def create_notes(
            self,
            subtitles: List[Subtitle],
            template: FlashCardTemplate,
            fields_content: Type[FlashCardFieldsContent]
    ) -> List[Note]:
        pass

    @abc.abstractmethod
    def append_notes_in_deck(self, deck: Deck, notes: List[Note]):
        pass

    def save_deck(self, deck: Deck, destination: str):
        FileUtils.validate_directory(destination)
        pass
