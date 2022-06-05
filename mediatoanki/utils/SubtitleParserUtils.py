from typing import Type, Union

from mediatoanki.model.subtitle_formats.Srt import Srt
from mediatoanki.model.subtitle_formats.SubtitleFormat import SubtitleFormat
from mediatoanki.model.subtitle_formats.Vtt import Vtt
from mediatoanki.utils.FileUtils import FileUtils


class SubtitleParserUtils:

    @staticmethod
    def get_subtitle_parser(subtitle_file: str) -> Type[SubtitleFormat]:
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
    ) -> Union[Type[SubtitleFormat], None]:
        return {
            "vtt": Vtt,
            "srt": Srt
        }.get(extension, None)
