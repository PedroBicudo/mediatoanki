import abc


class SubtitleFormat(metaclass=abc.ABCMeta):
    """Template que todos os formatos de legendas devem seguir.

    REGEX_LINE: Padrão para identificar o inicio de uma cena.
    ex
        00:00:00  -->  00:01:00 # REGEX_LINE detecta isso

    REGEX_TIME_START: Padrão para identificar o tempo em que a cena começou.
    ex
        00:00:00

    REGEX_TIME_END: Padrão para identificar o tempo em que a cena terminou.
    ex
        00:01:00

    """
    REGEX_LINE: str
    REGEX_TIME_START: str
    REGEX_TIME_END: str
