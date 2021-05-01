from typing import List
from src.model.Subtitle import Subtitle


def deep_copy_of_subs(subtitles: List[Subtitle]) -> List[Subtitle]:
    subtitles_copied = []
    for subtitle in subtitles:
        subtitles_copied.append(_instance_subtitle(subtitle))

    return subtitles_copied


def _instance_subtitle(subtitle_old: Subtitle) -> Subtitle:
    subtitle_new = Subtitle(subtitle_old.time_start, subtitle_old.time_end)
    subtitle_new.text = subtitle_old.text
    subtitle_new.audio = subtitle_old.audio
    subtitle_new.frame = subtitle_old.frame

    return subtitle_new
