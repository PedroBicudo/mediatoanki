import os
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path

from pysubs2 import SSAEvent

from mediatoanki.model.exceptions.ParseError import ParseError
from mediatoanki.parsers.srt.SrtParser import SrtParser


class SubtitleParserSrtTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.srt_parser = SrtParser()

    def test_srt_extract_subtitles_should_raise_exception_when_file_is_empty(
            self
    ):
        with tempfile.TemporaryDirectory() as tmp_dir:
            Path(tmp_dir, "sub.srt").touch()
            file_path = os.path.join(tmp_dir, "sub.srt")
            with open(file_path, "w") as tmp_file:
                tmp_file.write("")

            msg = (
                "Check if extract_subtitles from SrtParser"
                " raises an exception when file is empty"
            )
            with self.assertRaises(ParseError, msg=msg) as context:
                self.srt_parser.extract_subtitles(file_path)

            msg = (
                "Check if exception raised by extract_subtitle "
                "from SrtParser is correct"
            )
            expected = "No suitable formats"
            self.assertTrue(
                expected in str(context.exception),
                msg=msg
            )
            Path(tmp_dir, "sub.srt").unlink()

    def test_srt_convert_caption_to_subtitle(self):
        caption = SSAEvent(start=3600, end=4200, text="foo")

        subtitle = self.srt_parser.convert_caption_to_subtitles([caption])[0]
        self.assertEqual(
            timedelta(milliseconds=caption.start).total_seconds(),
            subtitle.time_start.total_seconds(),
            msg=(
                "Check if caption.start_in_seconds is equal "
                "to subtitle.time_start.total_seconds()"
            )
        )

        self.assertEqual(
            timedelta(milliseconds=caption.end).total_seconds(),
            subtitle.time_end.total_seconds(),
            msg=(
                "Check if caption.end_in_seconds is equal "
                "to subtitle.time_end.total_seconds()"
            )
        )

    def test_vtt_convert_caption_to_subtitle_text_without_breaks(self):
        caption = SSAEvent(start=3600, end=4200, text="foo.\nfoo")

        subtitle = self.srt_parser.convert_caption_to_subtitles([caption])[0]
        expected = "foo.foo"
        self.assertEqual(
            expected, subtitle.text,
            msg="Check if subtitle.text is correct"
        )

        caption.text = "foo.\n\nfoo"

        subtitle = self.srt_parser.convert_caption_to_subtitles([caption])[0]
        expected = "foo.foo"
        self.assertEqual(
            expected, subtitle.text,
            msg="Check if subtitle.text is correct"
        )


if __name__ == '__main__':
    unittest.main()
