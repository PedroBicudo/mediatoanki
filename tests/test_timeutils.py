import unittest
from datetime import timedelta

from src.utils.TimeUtils import TimeUtils


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.time_start = timedelta(hours=1, minutes=2, seconds=3)
        self.time_end = timedelta(hours=3, minutes=2, seconds=1)
        self.timeutil = TimeUtils(self.time_start, self.time_end)

    def test_time_start_is_less_than_time_end(self):
        time_start_correct = self.time_start
        time_end_correct = self.time_end

        result = TimeUtils.is_time_range_valid(
            time_start_correct.total_seconds(), time_end_correct.total_seconds()
        )
        self.assertEqual(result, True, msg="Teste: time_start < time_end")

    def test_time_end_is_more_than_time_start(self):
        time_start_wrong = self.time_end
        time_end_wrong = self.time_start
        result = TimeUtils.is_time_range_valid(
            time_start_wrong.total_seconds(), time_end_wrong.total_seconds()
        )
        self.assertEqual(result, False, msg="Teste: time_end < time_start")

    def test_time_start_is_equal_to_time_end(self):
        time_start_equal = time_end_equal = self.time_start
        result = TimeUtils.is_time_range_valid(
            time_start_equal.total_seconds(), time_end_equal.total_seconds()
        )
        self.assertEqual(result, True, msg="Text: time_start == time_end")

    def test_time_start_is_negative(self):
        time_start_negative = timedelta(-10, -1, -1)
        time_end_positive = timedelta(10, 11, 12)
        result = TimeUtils.is_time_range_valid(
            time_start_negative.total_seconds(),
            time_end_positive.total_seconds()
        )
        self.assertEqual(result, False, msg="Teste: time_start < 0")

    def test_is_time_start_with_pad_valid(self):
        seconds_added = timedelta(hours=1)
        result = self.timeutil.is_pad_start_invalid_with(seconds_added)
        self.assertEqual(result, False, msg=f"Teste: time_start + pad < time_end")

    def test_is_time_start_with_pad_more_than_time_end(self):
        seconds_added = timedelta(hours=10)
        result = self.timeutil.is_pad_start_invalid_with(seconds_added)
        self.assertEqual(result, True, msg=f"Teste: 10 horas adicionadas ao time_start")

    def test_is_time_start_with_pad_negative(self):
        seconds_added = timedelta(hours=-10)
        result = self.timeutil.is_pad_start_invalid_with(seconds_added)
        self.assertEqual(result, True, msg=f"Teste: -10 horas adicionadas ao time_start")

    def test_is_time_end_with_pad_valid(self):
        seconds_added = timedelta(hours=2)
        result = self.timeutil.is_pad_end_invalid_with(seconds_added)
        self.assertEqual(result, False, msg=f"Teste: time_end + pad > time_start")

    def test_is_time_end_less_than_time_start_with_pad(self):
        seconds_added = timedelta(hours=-10)
        result = self.timeutil.is_pad_end_invalid_with(seconds_added)
        self.assertEqual(result, True, msg="Teste: time_end < time_start")

    def test_is_time_end_negative(self):
        seconds_added = timedelta(hours=-10)
        result = self.timeutil.is_pad_end_invalid_with(seconds_added)
        self.assertEqual(result, True, msg="Teste: -10 horas adicionadas ao time_end")


if __name__ == '__main__':
    unittest.main()
