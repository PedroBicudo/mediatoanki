import unittest
from datetime import timedelta
from unittest import mock

from genanki import Note

from mediatoanki.deck.anki.AnkiDeckGenerator import AnkiDeckGenerator
from mediatoanki.deck.DeckGenerator import DeckGenerator
from mediatoanki.deck.flashcard.FlashCardTemplate import FlashCardTemplate
from mediatoanki.model.anki.FlashCardFieldsContent import \
    FlashCardFieldsContent
from mediatoanki.model.Subtitle import Subtitle
from mediatoanki.utils.FileUtils import FileUtils


class AnkiDeckGeneratorCase(unittest.TestCase):

    def setUp(self) -> None:
        self.model = FlashCardTemplate().model

    @mock.patch.object(FileUtils, "validate_directory")
    def test_create_deck(self, *args):
        under_test: DeckGenerator = AnkiDeckGenerator(
            "foo",
            FlashCardTemplate(),
            FlashCardFieldsContent("1", "foo").html,
            [],
            "foo"
        )
        name = "test"
        deck = under_test.create_deck(name)
        self.assertEqual(
            name,
            deck.name,
            msg="Check if deck name is correct"
        )

    @mock.patch.object(FileUtils, "validate_directory")
    def test_create_notes_correct_size(self, *args):
        under_test: DeckGenerator = AnkiDeckGenerator(
            "foo",
            FlashCardTemplate(),
            FlashCardFieldsContent("1", "foo").html,
            [],
            "foo"
        )
        template = FlashCardTemplate()
        subtitle = Subtitle(start=timedelta(0), end=timedelta(1))
        subtitle.text = "foo"

        notes = under_test.create_notes(
            [subtitle], template, FlashCardFieldsContent
        )

        self.assertTrue(
            len(notes) == 1,
            msg="Check if notes length is 1"
        )

    @mock.patch.object(FileUtils, "validate_directory")
    def test_create_notes_correct_fields_content(self, *args):
        under_test: DeckGenerator = AnkiDeckGenerator(
            "foo",
            FlashCardTemplate(),
            FlashCardFieldsContent("1", "foo").html,
            [],
            "foo"
        )
        template = FlashCardTemplate()
        subtitle = Subtitle(start=timedelta(0), end=timedelta(1))
        subtitle.text = "foo"

        notes = under_test.create_notes(
            [subtitle], template, FlashCardFieldsContent
        )

        expected = Note(
            model=template,
            fields=FlashCardFieldsContent(
                subtitle.id, subtitle.text
            ).html
        )

        self.assertListEqual(
            expected.fields, notes[0].fields,
            msg="Check if note fields are equal"
        )

    @mock.patch.object(FileUtils, "validate_directory")
    def test_create_notes_correct_model_content(self, *args):
        under_test: DeckGenerator = AnkiDeckGenerator(
            "foo",
            FlashCardTemplate(),
            FlashCardFieldsContent("1", "foo").html,
            [],
            "foo"
        )
        template = FlashCardTemplate()
        subtitle = Subtitle(start=timedelta(0), end=timedelta(1))
        subtitle.text = "foo"

        notes = under_test.create_notes(
            [subtitle], template, FlashCardFieldsContent
        )

        expected = Note(
            model=template.model,
            fields=FlashCardFieldsContent(
                subtitle.id, subtitle.text
            ).html
        )

        self.assertEqual(
            expected.model, notes[0].model,
            msg="Check if note models are equal"
        )

    @mock.patch.object(FileUtils, "validate_directory")
    def test_append_notes_in_deck_correct_size(self, *args):
        under_test: DeckGenerator = AnkiDeckGenerator(
            "foo",
            FlashCardTemplate(),
            FlashCardFieldsContent("1", "foo").html,
            [],
            "foo"
        )
        template = FlashCardTemplate()
        subtitle = Subtitle(start=timedelta(0), end=timedelta(1))
        subtitle.text = "foo"
        deck = under_test.create_deck("foo")
        notes = [Note(
            model=template,
            fields=FlashCardFieldsContent(
                subtitle.id, subtitle.text
            ).html
        )]

        under_test.append_notes_in_deck(deck, notes)
        self.assertTrue(
            len(deck.notes) == 1,
            msg="Check if appended notes have length 1"
        )

    @mock.patch.object(FileUtils, "validate_directory")
    def test_append_notes_in_deck_same_content(self, *args):
        under_test: DeckGenerator = AnkiDeckGenerator(
            "foo",
            FlashCardTemplate(),
            FlashCardFieldsContent("1", "foo").html,
            [],
            "foo"
        )
        template = FlashCardTemplate()
        subtitle = Subtitle(start=timedelta(0), end=timedelta(1))
        subtitle.text = "foo"
        deck = under_test.create_deck("foo")
        notes = [Note(
            model=template,
            fields=FlashCardFieldsContent(
                subtitle.id, subtitle.text
            ).html
        )]

        under_test.append_notes_in_deck(deck, notes)
        self.assertEqual(
            notes[0], deck.notes[0],
            msg=(
                "Check if appended notes in deck a"
                "re equal to created notes"
            )
        )


if __name__ == '__main__':
    unittest.main()
