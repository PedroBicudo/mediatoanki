from typing import List

from mediatoanki.model.Subtitle import Subtitle
from mediatoanki.model.file.Frame import Frame
from mediatoanki.model.file.Video import Video
from mediatoanki.utils.CopyUtils import deep_copy_of_subs


class SubtitleFrameExtractor:

    def __init__(self, video: Video):
        self._video = video

    def get_subtitles_with_one_frame_representing_each_subtitle(self, subtitles: List[Subtitle]) -> List[Subtitle]:
        if self._is_subtitles_valid(subtitles):
            return self._get_subtitles_with_defined_frames(subtitles)

        raise

    @staticmethod
    def _is_subtitles_valid(subtitles: List[Subtitle]) -> bool:
        return len(subtitles) > 0

    def _get_subtitles_with_defined_frames(self, subtitles: List[Subtitle]) -> List[Subtitle]:
        subs_with_frames = deep_copy_of_subs(subtitles)

        for pos, sub in enumerate(subtitles):
            print(f"Extracting frame from scene {sub.subtitle_id}...", end="")
            middle_sec_from_subs = ((sub.time_start + sub.time_end) // 2).total_seconds()
            subs_with_frames[pos].frame = Frame(self._video, middle_sec_from_subs)
            print("Done")

        return subs_with_frames
