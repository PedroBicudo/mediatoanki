from datetime import timedelta


class TimeUtils:

    def __init__(self, time_start: timedelta, time_end: timedelta):
        self._time_start = time_start
        self._time_end = time_end

    @staticmethod
    def is_time_range_valid(time_start: float, time_end: float) -> bool:
        return time_start <= time_end

    def is_pad_start_invalid_with(self, seconds_added: timedelta) -> bool:
        return (
            self.is_pad_negative_with(seconds_added) or
            self.is_pad_start_more_than_pad_end_with(seconds_added)
        )

    def is_pad_start_more_than_pad_end_with(self, seconds_added: timedelta) -> bool:
        return self._time_start + seconds_added >= self._time_end

    def is_pad_end_invalid_with(self, seconds_added: timedelta) -> bool:
        return (
                self.is_pad_negative_with(seconds_added) or
                self.is_pad_end_less_than_pad_start_with(seconds_added)
        )

    def is_pad_end_less_than_pad_start_with(self, seconds_added: timedelta) -> bool:
        return self._time_end + seconds_added <= self._time_start

    def is_pad_negative_with(self, seconds_added: timedelta) -> bool:
        return self._time_start + seconds_added < timedelta(seconds=0)
