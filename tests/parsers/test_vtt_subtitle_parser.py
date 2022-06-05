import os
import tempfile
import unittest
from pathlib import Path

from webvtt import Caption

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
            expected = "The file is empty."
            self.assertTrue(
                expected in str(context.exception),
                msg=msg
            )
            Path(tmp_dir, "sub.vtt").unlink()

    def test_vtt_convert_caption_to_subtitle(self):
        caption = Caption(start="21:54.280", end="21:56.339")
        caption.text = "foo"

        subtitle = self.vtt_parser.convert_caption_to_subtitles([caption])[0]
        self.assertEqual(
            caption.start_in_seconds, subtitle.time_start.total_seconds(),
            msg=(
                "Check if caption.start_in_seconds is equal "
                "to subtitle.time_start.total_seconds()"
            )
        )

        self.assertEqual(
            caption.end_in_seconds, subtitle.time_end.total_seconds(),
            msg=(
                "Check if caption.end_in_seconds is equal "
                "to subtitle.time_end.total_seconds()"
            )
        )

    def test_vtt_convert_caption_to_subtitle_text_without_breaks(self):
        caption = Caption(start="21:54.280", end="21:56.339")
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
