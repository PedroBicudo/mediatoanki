import unittest
from unittest import mock

from mediatoanki.model.subtitle_formats.SubtitleFormat import SubtitleFormat
from mediatoanki.utils.FileUtils import FileUtils
from mediatoanki.utils.SubtitleParserUtils import SubtitleParserUtils


class SubtitleParserUtilsTestCase(unittest.TestCase):

    @mock.patch.object(FileUtils, "validate_file")
    def test_get_subtitle_parser_with_not_supported_subtitle_extension(
            self, *args
    ):
        msg = (
            "Check if get_subtitle_parser raises "
            "exception when subtitle extension is not supported"
        )
        with self.assertRaises(NotImplementedError, msg=msg) as context:
            SubtitleParserUtils.get_subtitle_parser("foo.png")

        msg = (
            "Check if exception raised by "
            "get_subtitle_parser is correct"
        )
        expected = "Subtitle with png extension is not supported"
        self.assertTrue(expected in str(context.exception), msg=msg)

    @mock.patch.object(FileUtils, "validate_file")
    def test_get_subtitle_parser_should_return_subtitle_format_class(
            self, *args
    ):
        file = "a.vtt"
        subtitle_format = SubtitleParserUtils.get_subtitle_parser(file)
        self.assertTrue(
            issubclass(subtitle_format, SubtitleFormat),
            msg=(
                "Check if vtt extension returns a "
                "SubtitleFormat subclass"
            )
        )

        file = "a.srt"
        subtitle_format = SubtitleParserUtils.get_subtitle_parser(file)
        self.assertTrue(
            issubclass(subtitle_format, SubtitleFormat),
            msg=(
                "Check if srt extension returns a "
                "SubtitleFormat subclass"
            )
        )


if __name__ == '__main__':
    unittest.main()
