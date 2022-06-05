from typing import Union

from mediatoanki.parsers.srt.SrtParser import SrtParser
from mediatoanki.parsers.SubtitleParserAdapter import SubtitleParserAdapter
from mediatoanki.parsers.vtt.VttParser import VttParser
from mediatoanki.utils.FileUtils import FileUtils


class SubtitleParserUtils:

    @staticmethod
    def get_subtitle_parser(subtitle_file: str) -> SubtitleParserAdapter:
        FileUtils.validate_file(subtitle_file)
        extension = FileUtils.extract_extension(subtitle_file)
        parser = SubtitleParserUtils.supported_extensions(
            extension
        )
        if parser is None:
            raise NotImplementedError(
                f"Subtitle with {extension} extension is not supported"
            )

        return parser

    @staticmethod
    def supported_extensions(
            extension: str
    ) -> Union[SubtitleParserAdapter, None]:
        return {
            "vtt": VttParser(),
            "srt": SrtParser()
        }.get(extension, None)
