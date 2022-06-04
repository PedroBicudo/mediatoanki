import unittest
from unittest import mock

from mediatoanki.model.exceptions.FileIsNotAvideo import FileIsNotAvideo
from mediatoanki.utils.FileUtils import FileUtils


class FileUtilsCase(unittest.TestCase):

    @mock.patch("os.path.exists", return_value=False)
    def test_validate_directory_not_found(self, *args):
        with self.assertRaises(
            FileNotFoundError,
            msg="Check if directory is not found"
        ) as context:
            FileUtils.validate_directory("foo")

        self.assertTrue(
            "Directory not found" in str(context.exception),
            msg=(
                "Check if validate_directory message is correct"
            )
        )

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.path.isdir", return_value=False)
    def test_validate_directory_is_not_dir(self, *args):
        msg = "Check if path is not a directory"
        with self.assertRaises(
                NotADirectoryError,
                msg=msg
        ) as context:
            FileUtils.validate_directory("foo")

        msg = "The provided path is not a directory"
        self.assertTrue(
            msg in str(context.exception),
            msg=(
                "Check if validate_directory message is correct"
            )
        )

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.path.isdir", return_value=True)
    @mock.patch("os.access", return_value=False)
    def test_validate_diretory_has_permission(self, *args):
        msg = "Check if user has permission to access the directory"
        with self.assertRaises(
                PermissionError,
                msg=msg
        ) as context:
            FileUtils.validate_directory("foo")

        msg = "You don't have permission to access this directory"
        self.assertTrue(msg in str(context.exception))

    @mock.patch("os.path.exists", return_value=False)
    def test_validate_file_not_found(self, *args):
        with self.assertRaises(
            FileNotFoundError,
            msg="Check if file is not found"
        ) as context:
            FileUtils.validate_file("foo")

        self.assertTrue(
            "File not found" in str(context.exception),
            msg=(
                "Check if validate_file message is correct"
            )
        )

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.path.isfile", return_value=False)
    def test_validate_file_is_not_file(self, *args):
        msg = "Check if path is not a file"
        with self.assertRaises(
                FileNotFoundError,
                msg=msg
        ) as context:
            FileUtils.validate_file("foo")

        msg = "The provided path is not a file"
        self.assertTrue(
            msg in str(context.exception),
            msg=(
                "Check if validate_file message is correct"
            )
        )

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.path.isfile", return_value=True)
    @mock.patch("os.access", return_value=False)
    def test_validate_file_has_permission(self, *args):
        msg = "Check if user has permission to access the file"
        with self.assertRaises(
                PermissionError,
                msg=msg
        ) as context:
            FileUtils.validate_file("foo")

        msg = "You don't have permission to use this file"
        self.assertTrue(
            msg in str(context.exception),
            msg=(
                "Check if validate_file message is correct"
            )
        )

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.path.isfile", return_value=True)
    @mock.patch("os.access", return_value=True)
    @mock.patch("magic.from_file", return_value="plain/text")
    def test_validate_video_is_not_video(self, *args):
        with self.assertRaises(FileIsNotAvideo) as context:
            FileUtils.validate_video("foo")

        msg = "The provided file is a not video"
        self.assertTrue(
            msg in str(context.exception),
            msg=(
                "Check if validate_video message is correct"
            )
        )

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.path.isfile", return_value=True)
    @mock.patch("os.access", return_value=True)
    @mock.patch("magic.from_file", return_value="video/mp4")
    def test_validate_video_is_correct_with_mp4_extension(self, *args):
        raised = False
        try:
            FileUtils.validate_video("foo")

        except FileIsNotAvideo:
            raised = True

        self.assertFalse(
            raised,
            msg=(
                "Check if validate_video does not raise "
                "exception with mp4 format"
            )
        )

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.path.isfile", return_value=True)
    @mock.patch("os.access", return_value=True)
    @mock.patch("magic.from_file", return_value="application/octet-stream")
    def test_validate_video_is_correct_with_octet_stream_mime_type(
            self, *args
    ):
        raised = False
        try:
            FileUtils.validate_video("foo")

        except FileIsNotAvideo:
            raised = True

        self.assertFalse(
            raised,
            msg=(
                "Check if validate_video does not raise "
                "exception with application/octet-stream mime"
            )
        )


if __name__ == '__main__':
    unittest.main()
