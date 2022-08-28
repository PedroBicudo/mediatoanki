from datetime import datetime, timedelta

from mediatoanki.model.entities.Audio import Audio
from mediatoanki.model.entities.Frame import Frame
from mediatoanki.utils.TimeUtils import TimeUtils


class Subtitle:

    _id: str = ""
    _start: timedelta = None
    _end: timedelta = None
    text: str = ""
    frame: Frame = None
    audio: Audio = None

    def __init__(self, start: timedelta, end: timedelta):
        self._start = start
        self._end = end
        self._id = (
            f"{datetime.now().strftime('%d%m%Y%H%M%S')}_"
            f"{self._start.total_seconds()}"
            f"{self._end.total_seconds()}"
        )

    @property
    def id(self) -> str:
        return self._id

    @property
    def start(self) -> timedelta:
        return self._start

    @property
    def end(self) -> timedelta:
        return self._end

    def add_pad_start(self, seconds: int):
        seconds_added = timedelta(seconds=seconds)
        pad_utils = TimeUtils(self._start, self._end)
        if not pad_utils.is_pad_start_invalid_with(seconds_added):
            self._start += seconds_added
        else:
            raise ValueError("pad_start value invalid.")

    def add_pad_end(self, seconds: int):
        seconds_added = timedelta(seconds=seconds)
        pad_utils = TimeUtils(self._start, self._end)
        if not pad_utils.is_pad_end_invalid_with(seconds_added):
            self._end += seconds_added
        else:
            raise ValueError("pad_end value invalid.")
