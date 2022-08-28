from typing import List

from mediatoanki.extractors.ExtractorContract import ExtractorContract
from mediatoanki.model.entities.Frame import Frame
from mediatoanki.model.entities.Subtitle import Subtitle
from mediatoanki.model.entities.Video import Video


class FramesExtractor(ExtractorContract):

    def extract(self, video: Video, subtitles: List[Subtitle]):
        if len(subtitles) == 0:
            raise ValueError(
                (
                    "It was not possible "
                    "to extract the frame, "
                    "the subtitles were not informed."
                )
            )

        for pos, sub in enumerate(subtitles):
            print(f"Extracting frame from scene {sub.id}...", end="")
            middle = ((sub.start + sub.end) // 2)
            middle_sec_from_subs = round(middle.total_seconds())
            subtitles[pos].frame = Frame(
                video,
                middle_sec_from_subs,
            )
            print("Done")
