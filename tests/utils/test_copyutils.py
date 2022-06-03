import unittest
from datetime import timedelta

from mediatoanki.model.Subtitle import Subtitle
from mediatoanki.utils.CopyUtils import copy_subtitle, deep_copy_of_subs


class CopyUtilsTestCase(unittest.TestCase):

    @staticmethod
    def get_subtitle_instance():
        return Subtitle(
                timedelta(1, 2, 3),
                timedelta(1, 2, 4)
            )

    def test_deep_copy_of_subs(self):
        dummies = [self.get_subtitle_instance() for _ in range(10)]
        copies = deep_copy_of_subs(dummies)
        self.assertNotEqual(
            dummies,
            copies,
            msg="As listas devem ser diferentes."
        )
        for dummy, copy in zip(dummies, copies):
            self._test_if_parameters_from_dummy_and_copy_are_correct(
                dummy, copy
            )

    def test_default_copy_subtitle(self):
        dummy = self.get_subtitle_instance()
        copy = copy_subtitle(dummy)
        self.assertNotEqual(
            dummy,
            copy,
            msg="Endereços de memória devem ser diferentes."
        )
        self._test_if_parameters_from_dummy_and_copy_are_correct(dummy, copy)

    def _test_if_parameters_from_dummy_and_copy_are_correct(
            self,
            dummy: Subtitle,
            copy: Subtitle
    ):
        self.assertEqual(
            dummy.time_start,
            copy.time_start,
            msg="time_start deve ser igual."
        )
        self.assertEqual(
            dummy.time_end,
            copy.time_end,
            msg="time_end deve ser igual."
        )
        self.assertEqual(
            dummy.text,
            copy.text,
            msg="text deve ser igual."
        )
        self.assertEqual(
            dummy.audio,
            copy.audio,
            msg=(
                 "audio deve conter o mesmo endereço de memória "
                 "ou serem ambos None."
            )
        )
        self.assertEqual(
            dummy.frame,
            copy.frame,
            msg=(
                "frame deve conter o mesmo endereço de memória "
                "ou serem ambos None."
            )
        )


if __name__ == '__main__':
    unittest.main()
