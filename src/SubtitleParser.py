import pathlib
import re
from datetime import timedelta
from typing import List

from src.model.Subtitle import Subtitle
from src.model.subtitle_formats.Srt import Srt
from src.model.subtitle_formats.SubtitleFormat import SubtitleFormat
from src.model.subtitle_formats.Vtt import Vtt


class SubtitleParser:

    def get_subtitles_from_file(self, filename: str) -> List[Subtitle]:
        file_format = SubtitleParser._get_file_format(filename).lower()
        subtitle_regex = self._get_regex_based_on_file_format(file_format)
        file_lines = self._get_subtitle_file_lines(filename)
        subtitles = []
        while self._is_not_empty(file_lines):
            current_line = file_lines.pop(0)
            if self._is_time_from_scene(current_line, subtitle_regex):
                current_subtitle = self._get_subtitle_with_times_defined(current_line, subtitle_regex)
                current_subtitle.text = self._get_text_from_scene(file_lines)
                subtitles.append(current_subtitle)

        return subtitles

    @staticmethod
    def _is_time_from_scene(text: str, subtitle_regex: SubtitleFormat) -> re:
        return re.match(subtitle_regex.REGEX_LINE, text)

    @staticmethod
    def _get_subtitle_with_times_defined(line_time: str, subtitle_regex: SubtitleFormat):
        time_start = SubtitleParser._get_timedelta_from(
            re.match(subtitle_regex.REGEX_TIME_START, line_time).group(0),
            subtitle_regex
        )
        time_end = SubtitleParser._get_timedelta_from(
            re.search(subtitle_regex.REGEX_TIME_END, line_time).group(0),
            subtitle_regex
        )

        return Subtitle(time_start, time_end)

    def _get_text_from_scene(self, file_lines: List[str]) -> str:
        text_after_time = file_lines.pop(0)
        text_scene = ""
        while self._is_not_empty(file_lines) and self._is_not_blank_line(text_after_time):
            text_scene += f" {text_after_time.strip()}"
            text_after_time = file_lines.pop(0)

        return text_scene

    def _is_not_blank_line(self, text: str):
        return self._is_not_empty(text.strip())

    @staticmethod
    def _is_not_empty(content: [List, str]):
        return len(content) > 0

    def _get_subtitle_file_lines(self, filename: str) -> List[str]:
        try:
            return self._get_lines_from_file(filename)

        except Exception as error:
            raise Exception("Não foi possível abrir o arquivo de legendas.")

    def _get_lines_from_file(self, filename: str) -> List[str]:
        file = open(filename, 'r')
        lines = list(file)
        file.close()
        return lines

    @staticmethod
    def _get_timedelta_from(time: str, subtitle_regex: SubtitleFormat) -> timedelta:
        hours, miliseconds = time.split(subtitle_regex.MILLISECONDS_DELIMITER)
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
    def _has_hour_field(time: str) -> bool:
        return time.count(":") == 2

    def _get_regex_based_on_file_format(self, file_format: str) -> SubtitleFormat:
        try:
            return SubtitleParser._get_subtitle_regex(file_format)
        except Exception as _:
            raise NotImplementedError(f"O formato '{file_format}' não está disponível")

    @staticmethod
    def _get_subtitle_regex(file_format: str) -> SubtitleFormat:
        subs_regex = {
            "vtt": Vtt,
            "srt": Srt
        }
        return subs_regex[file_format]

    @staticmethod
    def _get_file_format(filename: str) -> str:
        return pathlib.Path(filename).suffix.split(".")[-1]
