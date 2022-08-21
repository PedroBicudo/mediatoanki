import os

import chardet
import magic

from mediatoanki.model.exceptions.FileIsNotAvideo import FileIsNotAvideo


class FileUtils:

    NO_EXTENSION = ""

    @staticmethod
    def extract_encoding(path: str) -> str:
        FileUtils.validate_file(path)
        file = open(path, 'rb')
        file_binary = file.read()
        file.close()
        return chardet.detect(file_binary)["encoding"]

    @staticmethod
    def extract_extension(path: str) -> str:
        FileUtils.validate_file(path)
        _, extension = os.path.splitext(path)
        if extension == FileUtils.NO_EXTENSION:
            raise ValueError("File must have extension")

        return extension.split(".")[1].lower()

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
        mime_type = magic.from_file(path, mime=True)
        if "video" in mime_type:
            return

        if "octet-stream" in mime_type:
            return

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
