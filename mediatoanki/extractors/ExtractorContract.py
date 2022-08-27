import abc
from typing import List

from mediatoanki.model.file.Video import Video
from mediatoanki.model.Subtitle import Subtitle


class ExtractorContract(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def extract(self, video: Video, subtitles: List[Subtitle]):
        pass
