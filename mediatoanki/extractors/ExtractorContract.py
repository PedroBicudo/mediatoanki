import abc
from typing import List

from mediatoanki.model.file.Subtitle import Subtitle
from mediatoanki.model.file.Video import Video


class ExtractorContract(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def extract(self, video: Video, subtitles: List[Subtitle]):
        pass
