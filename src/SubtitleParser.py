import pathlib
import re
from datetime import timedelta
from typing import List
from src.model.Subtitle import Subtitle
from src.model.subtitle_formats.SubtitleFormat import SubtitleFormat
from src.model.subtitle_formats.Vtt import Vtt


class SubtitleParser:

    def get_subtitles_from_file(self, filename) -> List[Subtitle]:
        file_format = SubtitleParser._get_file_format(filename).lower()
        subtitle_regex = SubtitleParser._get_regex_based_on_file_format(file_format)
        file = open(filename, "r")
        subs = []
        for line in file.readlines():
            match = re.match(subtitle_regex.REGEX_LINE, line)
            if match:
                time_start = SubtitleParser._get_timedelta_from(
                    re.match(subtitle_regex.REGEX_TIME_START, line).group(0)
                )
                time_end = SubtitleParser._get_timedelta_from(
                    re.search(subtitle_regex.REGEX_TIME_END, line).group(0)
                )
                subs.append(Subtitle(time_start, time_end))
                continue

            if len(subs) > 0:
                subs[-1].text += f"{line.strip()} "

        return subs

    @staticmethod
    def _get_timedelta_from(time: str) -> timedelta:
        hours, miliseconds = time.split('.')
        if SubtitleParser._has_hour_field(time):
            hour, minute, second = hours.split(":")
            return timedelta(
                hours=float(hour),
                minutes=float(minute),
                seconds=float(second),
                milliseconds=float(miliseconds)
            )

        else:
            minute, second = hours.split(":")
            return timedelta(
                minutes=float(minute),
                seconds=float(second),
                milliseconds=float(miliseconds)
            )

    @staticmethod
    def _has_hour_field(time: str):
        return time.count(":") == 2

    def _get_regex_based_on_file_format(self, file_format) -> SubtitleFormat:
        try:
            return self._get_subtitle_regex(file_format)
        except Exception as _:
            raise NotImplementedError(f"O formato '{file_format}' não está disponível")

    @staticmethod
    def _get_subtitle_regex(file_format) -> SubtitleFormat:
        subs_regex = {
            "vtt": Vtt
        }
        return subs_regex[file_format]


    @staticmethod
    def _get_file_format(filename):
        return pathlib.Path(filename).suffix
