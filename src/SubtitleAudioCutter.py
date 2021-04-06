import logging
from typing import List

from src.model.Subtitle import Subtitle
from src.model.file.Audio import Audio
from src.model.file.Video import Video
from src.utils.CopyUtils import deep_copy_of_subs


class SubtitleAudioCutter:

    def __init__(self, video: Video):
        self.__video = video

    def get_subtitles_with_one_audio_representing_the_subtitle_scene(self, subtitles: List[Subtitle]) -> List[Subtitle]:
        subs_with_audio = deep_copy_of_subs(subtitles)
        for sub in subs_with_audio:

            print(f"Extracting audio from scene {sub.subtitle_id}...", end="")
            audio = self.__video.video.audio.subclip(
                sub.time_start.total_seconds(),
                sub.time_end.total_seconds()
            )
            sub.audio = Audio(audio)
            print("Done")

        return subs_with_audio
