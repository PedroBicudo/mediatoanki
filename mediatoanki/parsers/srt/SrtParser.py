from datetime import timedelta
from typing import List

import webvtt
from webvtt import Caption, MalformedFileError

from mediatoanki.model.exceptions.ParseError import ParseError
from mediatoanki.model.Subtitle import Subtitle
from mediatoanki.parsers.SubtitleParserAdapter import SubtitleParserAdapter


class SrtParser(SubtitleParserAdapter):

    def extract_subtitles(self, file: str) -> List[Subtitle]:
        try:
            captions = webvtt.from_srt(file)
            return self.convert_caption_to_subtitles(captions)

        except MalformedFileError as e:
            raise ParseError(e)

        except FileNotFoundError:
            raise FileNotFoundError("File not found")

        except PermissionError:
            raise PermissionError(
                "You don't have permission to use this file"
            )

        except RuntimeError as e:
            raise RuntimeError(e)

    def convert_caption_to_subtitles(
            self,
            captions: List[Caption]
    ) -> List[Subtitle]:
        subtitles = []
        for caption in captions:
            subtitle = Subtitle(
                time_start=timedelta(seconds=caption.start_in_seconds),
                time_end=timedelta(seconds=caption.end_in_seconds)
            )
            subtitle.text = "".join(caption.text.split("\n"))
            subtitles.append(subtitle)

        return subtitles
