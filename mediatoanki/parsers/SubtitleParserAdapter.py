import abc
from typing import List

from mediatoanki.model.Subtitle import Subtitle


class SubtitleParserAdapter(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def extract_subtitles(self, file: str) -> List[Subtitle]:
        pass