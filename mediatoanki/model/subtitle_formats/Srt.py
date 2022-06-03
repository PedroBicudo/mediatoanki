from mediatoanki.model.subtitle_formats.SubtitleFormat import SubtitleFormat


class Srt(SubtitleFormat):
    REGEX_LINE: str = (
        r"^\d{2}:\d{2}:\d{2}(,\d{3}|)[ ]{1,}-->[ ]{1,}"
        r"\d{2}:\d{2}:\d{2}(,\d{3}|)$"
    )
    REGEX_TIME_START: str = r"^\d{2}:\d{2}:\d{2}(,\d{3}|)"
    REGEX_TIME_END: str = r"\d{2}:\d{2}:\d{2}(,\d{3}|)$"
    MILLISECONDS_DELIMITER = ","
