import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from mediatoanki.model.exceptions.FileIsNotAvideo import FileIsNotAvideo
from mediatoanki.utils.FileUtils import FileUtils


class FileUtilsCase(unittest.TestCase):

    def test_extract_encoding(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            Path(tmp_dir, "sub_iso8859.srt").touch()
            Path(tmp_dir, "sub_utf8.srt").touch()
            file_path_iso = os.path.join(tmp_dir, "sub_iso8859.srt")
            file_path_utf = os.path.join(tmp_dir, "sub_utf8.srt")

            with open(file_path_iso, "w", encoding="iso-8859-1") as tmp_file:
                tmp_file.write(
                    (
                        "98"
                        "00:05:07,400 --> 00:05:10,400"
                        "Chocolate cake à la Blake"
                    ))

            self.assertEqual(
                "ISO-8859-1",
                FileUtils.extract_encoding(file_path_iso),
                msg="Check if encoding is iso-8859-1"
            )

            with open(file_path_utf, "w", encoding="utf-8") as tmp_file:
                tmp_file.write(
                    (
                        "1"
                        "00:00:02, 600 --> 00:00:05, 900"
                        "It seems today that all you see"

                    ))

            self.assertEqual(
                "ascii",
                FileUtils.extract_encoding(file_path_utf),
                msg="Check if encoding is us-ascii"
            )

            Path(tmp_dir, "sub_iso8859.srt").unlink()
            Path(tmp_dir, "sub_utf8.srt").unlink()

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

    @mock.patch.object(FileUtils, "validate_file")
    def test_extract_extension_invalid_with_no_extension(self, *args):
        file = "foo"

        msg = (
            "Check if exception is raised "
            "when file does not have extension"
        )

        with self.assertRaises(ValueError, msg=msg) as context:
            FileUtils.extract_extension(file)

        msg = "File must have extension"
        self.assertTrue(
            msg in str(context.exception),
            msg=(
                "Check if extract_extension "
                "exception message is correct"
            )
        )

    @mock.patch.object(FileUtils, "validate_file")
    def test_extract_extension_with_vtt_dot_png_file(self, *args):
        file = "foo.vtt.png"

        extension = FileUtils.extract_extension(file)
        expected = "png"

        msg = "extract extension should return png"
        self.assertEqual(expected, extension, msg=msg)

    @mock.patch.object(FileUtils, "validate_file")
    def test_extract_extension_with_uppercase_png(self, *args):
        file = "foo.PNG"

        extension = FileUtils.extract_extension(file)
        expected = "png"

        msg = "extract extension should return lowercase png"
        self.assertEqual(expected, extension, msg=msg)

    @mock.patch.object(FileUtils, "validate_file")
    def test_extract_extension_with_capitalized_png(self, *args):
        file = "foo.Png"

        extension = FileUtils.extract_extension(file)
        expected = "png"

        msg = "extract extension should return lowercase png"
        self.assertEqual(expected, extension, msg=msg)


if __name__ == '__main__':
    unittest.main()
