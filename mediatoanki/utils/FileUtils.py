import os

import magic

from mediatoanki.model.exceptions.FileIsNotAvideo import FileIsNotAvideo


class FileUtils:

    @staticmethod
    def validate_directory(path: str):
        if not os.path.exists(path):
            raise FileNotFoundError("Directory not found")

        if not os.path.isdir(path):
            raise NotADirectoryError(
                "The provided path is not a directory"
            )

        if not (os.access(path, os.R_OK) and os.access(path, os.W_OK)):
            raise PermissionError(
                "You don't have permission to access this directory"
            )

    @staticmethod
    def validate_video(path: str):
        FileUtils.validate_file(path)
        if "video" not in magic.from_file(path, mime=True):
            raise FileIsNotAvideo("The provided file is a not video")

    @staticmethod
    def validate_file(path: str):
        if not os.path.exists(path):
            raise FileNotFoundError("File not found")

        if not os.path.isfile(path):
            raise FileNotFoundError(
                "The provided path is not a file"
            )

        if not (os.access(path, os.R_OK) and os.access(path, os.W_OK)):
            raise PermissionError(
                "You don't have permission to use this file"
            )
