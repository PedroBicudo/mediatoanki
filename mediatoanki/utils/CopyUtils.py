from typing import List
from mediatoanki.model.Subtitle import Subtitle


def deep_copy_of_subs(subtitles: List[Subtitle]) -> List[Subtitle]:
    subtitles_copy: List[Subtitle] = []
    for subtitle in subtitles:
        subtitles_copy.append(copy_subtitle(subtitle))

    return subtitles_copy


def copy_subtitle(subtitle_old: Subtitle) -> Subtitle:
    subtitle_new = Subtitle(subtitle_old.time_start, subtitle_old.time_end)
    subtitle_new.text = subtitle_old.text
    subtitle_new.audio = subtitle_old.audio
    subtitle_new.frame = subtitle_old.frame

    return subtitle_new
