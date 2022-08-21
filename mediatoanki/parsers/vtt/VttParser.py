from datetime import timedelta
from typing import List

import pysubs2
from pysubs2 import Pysubs2Error, SSAEvent

from mediatoanki.model.exceptions.ParseError import ParseError
from mediatoanki.model.Subtitle import Subtitle
from mediatoanki.parsers.SubtitleParserAdapter import SubtitleParserAdapter
from mediatoanki.utils.FileUtils import FileUtils


class VttParser(SubtitleParserAdapter):

    def extract_subtitles(self, file: str) -> List[Subtitle]:
        try:
            file_encoding = FileUtils.extract_encoding(file)
            captions = list(pysubs2.load(file, encoding=file_encoding))
            return self.convert_caption_to_subtitles(captions)

        except FileNotFoundError:
            raise FileNotFoundError("File not found")

        except PermissionError:
            raise PermissionError(
                "You don't have permission to use this file"
            )

        except Pysubs2Error as e:
            raise ParseError(e)

        except RuntimeError as e:
            raise RuntimeError(e)

    def convert_caption_to_subtitles(
            self,
            captions: List[SSAEvent]
    ) -> List[Subtitle]:
        subtitles = []
        for caption in captions:
            subtitle = Subtitle(
                time_start=timedelta(milliseconds=caption.start),
                time_end=timedelta(milliseconds=caption.end)
            )
            subtitle.text = "".join(caption.text.split("\n"))
            subtitles.append(subtitle)

        return subtitles
