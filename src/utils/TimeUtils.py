from datetime import timedelta


class TimeUtils:

    def __init__(self, time_start: timedelta, time_end: timedelta):
        self._time_start = time_start
        self._time_end = time_end

    @staticmethod
    def is_time_range_valid(time_start: float, time_end: float) -> bool:
        return (
                time_start <= time_end and
                TimeUtils._is_time_positive(time_start) and
                TimeUtils._is_time_positive(time_end)
        )

    def is_pad_start_invalid_with(self, seconds_added: timedelta) -> bool:
        return (
            self._is_time_start_negative_with(seconds_added) or
            self._is_pad_start_more_than_pad_end_with(seconds_added)
        )

    def _is_pad_start_more_than_pad_end_with(self, seconds_added: timedelta) -> bool:
        time_start_new = self._time_start + seconds_added
        return time_start_new >= self._time_end

    def is_pad_end_invalid_with(self, seconds_added: timedelta) -> bool:
        return (
                self._is_time_end_negative_with(seconds_added) or
                self.is_pad_end_less_than_pad_start_with(seconds_added)
        )

    def is_pad_end_less_than_pad_start_with(self, seconds_added: timedelta) -> bool:
        return self._time_end + seconds_added <= self._time_start

    def _is_time_start_negative_with(self, seconds_added: timedelta):
        return self._is_timedelta_negative_with(self._time_start, seconds_added)

    def _is_time_end_negative_with(self, seconds_added: timedelta):
        return self._is_timedelta_negative_with(self._time_end, seconds_added)

    @staticmethod
    def _is_timedelta_negative_with(time: timedelta, seconds_added: timedelta):
        return time + seconds_added < timedelta(seconds=0)

    def is_pad_negative_with(self, seconds_added: timedelta) -> bool:
        return self._time_start + seconds_added < timedelta(seconds=0)

    @staticmethod
    def _is_time_positive(time: float):
        return time >= 0.0
