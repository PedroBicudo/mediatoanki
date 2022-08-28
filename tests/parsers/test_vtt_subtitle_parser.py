import os
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path

from pysubs2 import SSAEvent

from mediatoanki.model.exceptions.ParseError import ParseError
from mediatoanki.parsers.vtt.VttParser import VttParser


class SubtitleParserVttTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.vtt_parser = VttParser()

    def test_vtt_extract_subtitles_should_raise_exception_when_file_is_empty(
            self
    ):
        with tempfile.TemporaryDirectory() as tmp_dir:
            Path(tmp_dir, "sub.vtt").touch()
            file_path = os.path.join(tmp_dir, "sub.vtt")
            with open(file_path, "w") as tmp_file:
                tmp_file.write("")

            msg = (
                "Check if extract_subtitles from VttParser"
                " raises an exception when file is empty"
            )
            with self.assertRaises(ParseError, msg=msg) as context:
                self.vtt_parser.extract_subtitles(file_path)

            msg = (
                "Check if exception raised by extract_subtitle "
                "from VttParser is correct"
            )
            expected = "No suitable formats"
            self.assertTrue(
                expected in str(context.exception),
                msg=msg
            )
            Path(tmp_dir, "sub.vtt").unlink()

    def test_vtt_convert_caption_to_subtitle(self):
        caption = SSAEvent(start=3600, end=4200, text="foo")

        subtitle = self.vtt_parser.convert_caption_to_subtitles([caption])[0]
        self.assertEqual(
            timedelta(milliseconds=caption.start).total_seconds(),
            subtitle.start.total_seconds(),
            msg=(
                "Check if caption.start_in_seconds is equal "
                "to subtitle.start.total_seconds()"
            )
        )

        self.assertEqual(
            timedelta(milliseconds=caption.end).total_seconds(),
            subtitle.end.total_seconds(),
            msg=(
                "Check if caption.end_in_seconds is equal "
                "to subtitle.end.total_seconds()"
            )
        )

    def test_vtt_convert_caption_to_subtitle_text_without_breaks(self):
        caption = SSAEvent(start=3600, end=4200, text="foo.\nfoo")
        caption.text = "foo.\nfoo"

        subtitle = self.vtt_parser.convert_caption_to_subtitles([caption])[0]
        expected = "foo.foo"
        self.assertEqual(
            expected, subtitle.text,
            msg="Check if subtitle.text is correct"
        )

        caption.text = "foo.\n\nfoo"

        subtitle = self.vtt_parser.convert_caption_to_subtitles([caption])[0]
        expected = "foo.foo"
        self.assertEqual(
            expected, subtitle.text,
            msg="Check if subtitle.text is correct"
        )


if __name__ == '__main__':
    unittest.main()
