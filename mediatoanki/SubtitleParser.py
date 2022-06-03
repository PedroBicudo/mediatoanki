import pathlib
import re
from datetime import timedelta
from typing import List

from mediatoanki.model.Subtitle import Subtitle
from mediatoanki.model.subtitle_formats.Srt import Srt
from mediatoanki.model.subtitle_formats.SubtitleFormat import SubtitleFormat
from mediatoanki.model.subtitle_formats.Vtt import Vtt


class SubtitleParser:

    def get_subtitles_from_file(self, filename: str) -> List[Subtitle]:
        file_format = SubtitleParser._get_file_format(filename).lower()
        subtitle_regex = self._get_regex_based_on_file_format(file_format)
        file_lines = self._get_subtitle_file_lines(filename)
        subtitles = []
        while self._is_not_empty(file_lines):
            current_line = file_lines.pop(0)
            if self._is_time_from_scene(current_line, subtitle_regex):
                current_subtitle = self._get_subtitle_with_times_defined(
                    current_line, subtitle_regex
                )
                current_subtitle.text = self._get_text_from_scene(file_lines)
                subtitles.append(current_subtitle)

        return subtitles

    @staticmethod
    def _is_time_from_scene(text: str, subtitle_regex: SubtitleFormat) -> re:
        return re.match(subtitle_regex.REGEX_LINE, text)

    @staticmethod
    def _get_subtitle_with_times_defined(
            line_time: str,
            subtitle_regex: SubtitleFormat
    ):
        time_start = SubtitleParser.convert_time_text_to_timedelta(
            re.match(subtitle_regex.REGEX_TIME_START, line_time).group(0),
            subtitle_regex
        )
        time_end = SubtitleParser.convert_time_text_to_timedelta(
            re.search(subtitle_regex.REGEX_TIME_END, line_time).group(0),
            subtitle_regex
        )

        return Subtitle(time_start, time_end)

    def _get_text_from_scene(self, file_lines: List[str]) -> str:
        if not self._is_not_empty(file_lines):
            return ""

        text_scene = file_lines.pop(0).strip()
        text_after_time = text_scene
        while self._is_not_empty(file_lines) and \
                self._is_not_blank_line(text_after_time):
            text_after_time = file_lines.pop(0).strip()
            text_scene += f" {text_after_time}"

        return text_scene.strip()

    def _is_not_blank_line(self, text: str):
        return self._is_not_empty(text.strip())

    @staticmethod
    def _is_not_empty(content: [List, str]):
        return len(content) > 0

    def _get_subtitle_file_lines(self, filename: str) -> List[str]:
        try:
            return self._get_lines_from_file(filename)

        except Exception:
            raise Exception("Não foi possível abrir o arquivo de legendas.")

    def _get_lines_from_file(self, filename: str) -> List[str]:
        file = open(filename, 'r')
        lines = list(file)
        file.close()
        return lines

    @staticmethod
    def convert_time_text_to_timedelta(
            time: str,
            subtitle_regex: SubtitleFormat
    ) -> timedelta:
        time_list = SubtitleParser._get_default_time_list()
        time_split = SubtitleParser\
            ._get_hours_milliseconds_splitted(
                time, subtitle_regex
            )
        SubtitleParser._update_hours(time_list, *time_split)
        return SubtitleParser._convert_time_list_to_timedelta(time_list)

    @staticmethod
    def _get_hours_milliseconds_splitted(
            time: str,
            subtitle_regex: SubtitleFormat
    ):
        return time.split(subtitle_regex.MILLISECONDS_DELIMITER)

    @staticmethod
    def _get_default_time_list():
        return [
            0.0,  # hour
            0.0,  # minute
            0.0,  # second
            0.0   # milliseconds
        ]

    @staticmethod
    def _update_hours(time_list: dict, hours: str, milliseconds: str = None):
        SubtitleParser._update_milliseconds_in_time_list(
            time_list, milliseconds
        )
        SubtitleParser._update_hours_in_time_list(time_list, hours)

    @staticmethod
    def _update_milliseconds_in_time_list(time_list: dict, milliseconds: str):
        if milliseconds is not None:
            time_list[3] = float(milliseconds)

    @staticmethod
    def _update_hours_in_time_list(time_list: dict, hours: str):
        if SubtitleParser._has_hour_field(hours):
            hour, minute, second = hours.split(":")
            time_list[0] = float(hour)
            time_list[1] = float(minute)
            time_list[2] = float(second)

        else:
            minute, second = hours.split(":")
            time_list[1] = float(minute)
            time_list[2] = float(second)

    @staticmethod
    def _convert_time_list_to_timedelta(time_list: dict) -> timedelta:
        return timedelta(
                hours=time_list[0],
                minutes=time_list[1],
                seconds=time_list[2],
                milliseconds=time_list[3]
        )

    @staticmethod
    def _has_hour_field(time: str) -> bool:
        return time.count(":") == 2

    def _get_regex_based_on_file_format(
            self, file_format: str
    ) -> SubtitleFormat:
        sub_format = SubtitleParser._get_subtitle_regex(file_format)
        if sub_format is not None:
            return sub_format

        raise NotImplementedError(
            f"O formato '{file_format}' não está disponível"
        )

    @staticmethod
    def _get_subtitle_regex(file_format: str) -> SubtitleFormat:
        subs_regex = {
            "vtt": Vtt,
            "srt": Srt
        }

        return subs_regex.get(file_format, None)

    @staticmethod
    def _get_file_format(filename: str) -> str:
        return pathlib.Path(filename).suffix.split(".")[-1]
