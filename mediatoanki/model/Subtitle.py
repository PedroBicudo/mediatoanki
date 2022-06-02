from datetime import timedelta, datetime

from mediatoanki.model.file.Audio import Audio
from mediatoanki.model.file.Frame import Frame
from mediatoanki.utils.TimeUtils import TimeUtils


class Subtitle:

    _text: str = ""
    _frame: Frame = None
    _audio: Audio = None

    def __init__(self, time_start: timedelta, time_end: timedelta):
        self._validate_time_range(time_start, time_end)
        self._scene_id = f"{self._time_start.total_seconds()}{self._time_end.total_seconds()}"
        self._datetime_id = datetime.now().strftime("%d%m%Y%H%M%S")

    def _validate_time_range(self, time_start: timedelta, time_end: timedelta):
        if not TimeUtils.is_time_range_valid(time_start.total_seconds(), time_end.total_seconds()):
            raise ValueError("time range (seconds_start -> seconds_stop) invalid.")

        self._time_start: timedelta = time_start
        self._time_end: timedelta = time_end

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, frame: Frame):
        self._frame = frame

    @property
    def audio(self):
        return self._audio

    @audio.setter
    def audio(self, audio: Audio):
        self._audio = audio

    @property
    def time_start(self):
        return self._time_start

    @property
    def time_end(self):
        return self._time_end

    @property
    def subtitle_id(self):
        return f"{self._datetime_id}_{self._scene_id}"

    def add_pad_start(self, seconds: int):
        seconds_added = timedelta(seconds=seconds)
        pad_utils = TimeUtils(self.time_start, self.time_end)
        if not pad_utils.is_pad_start_invalid_with(seconds_added):
            self._time_start += seconds_added
        else:
            raise ValueError("pad_start value invalid.")

    def add_pad_end(self, seconds: int):
        seconds_added = timedelta(seconds=seconds)
        pad_utils = TimeUtils(self.time_start, self.time_end)
        if not pad_utils.is_pad_end_invalid_with(seconds_added):
            self._time_end += seconds_added
        else:
            raise ValueError("pad_end value invalid.")