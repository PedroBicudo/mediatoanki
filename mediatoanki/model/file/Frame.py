import os

from mediatoanki.model.file.File import File
from mediatoanki.model.file.Video import Video


class Frame(File):

    def __init__(self, video: Video, frame_second: int):
        self._video = video
        self._frame_second = frame_second

    def write_at(self, name: str, dir_destination: str):
        print("\tSaving frame...", end="")
        try:
            self._write_file(name, dir_destination)
            print("Done")

        except Exception:
            print("Failed")

    def _write_file(self, name: str, dir_destination: str):
        path = os.path.join(dir_destination, f"{name}.png")
        self._video.video.save_frame(path, t=self._frame_second)
