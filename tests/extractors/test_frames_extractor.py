import unittest
from unittest import mock

from mediatoanki.extractors.frame.FramesExtractor import FramesExtractor


class FramesExtractorTestCase(unittest.TestCase):

    @mock.patch("mediatoanki.model.entities.Video", autospec=True)
    def test_empty_subtitles_throw_ValueError_exception(self, video):
        with self.assertRaises(
                ValueError,
                msg=(
                        "Check if ValueError is"
                        "raised when subtitles is empty"
                )
        ) as exception:
            FramesExtractor().extract(video, [])

        self.assertTrue(
            (
                "It was not possible to extract the frame, "
                "the subtitles were not informed."
            ) in str(exception.exception)
        )


if __name__ == '__main__':
    unittest.main()
