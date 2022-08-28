from typing import List

from mediatoanki.extractors.ExtractorContract import ExtractorContract
from mediatoanki.model.file.Audio import Audio
from mediatoanki.model.file.Subtitle import Subtitle
from mediatoanki.model.file.Video import Video


class AudiosExtractor(ExtractorContract):

    def extract(self, video: Video, subtitles: List[Subtitle]):
        if len(subtitles) == 0:
            raise ValueError(
                (
                    "It was not possible "
                    "to extract the audio, "
                    "the subtitles were not informed."
                )
            )

        for subtitle in subtitles:
            print(
                f"Extracting audio from scene {subtitle.id}...",
                end=""
            )
            audio = video.video.audio.subclip(
                subtitle.start.total_seconds(),
                subtitle.end.total_seconds()
            )
            subtitle.audio = Audio(audio)
            print("Done")
