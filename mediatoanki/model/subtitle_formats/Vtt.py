from mediatoanki.model.subtitle_formats.SubtitleFormat import SubtitleFormat


class Vtt(SubtitleFormat):
    REGEX_LINE: str = (
        r"^([0-9]{2}:|)[0-9]{2}:[0-9]{2}\.[0-9]{3}[ ]{1,}-{1,}>[ ]{1,}"
        r"([0-9]{2}:|)[0-9]{2}:[0-9]{2}\.[0-9]{3}$"
    )
    REGEX_TIME_START: str = r"^([0-9]{2}:|)[0-9]{2}:[0-9]{2}\.[0-9]{3}"
    REGEX_TIME_END: str = r"([0-9]{2}:|)[0-9]{2}:[0-9]{2}\.[0-9]{3}$"
    MILLISECONDS_DELIMITER = "."
