import os
from src.model.file.File import File
from src.model.file.Video import Video


class Frame(File):

    def __init__(self, video: Video, frame_second: int):
        self._video = video
        self._frame_second = frame_second

    def write_at(self, name: str, dir_destination: str):
        print(f"\tSaving frame...", end="")
        try:
            self._write_file(name, dir_destination)
            print("Done")

        except Exception as error:
            print("Failed")

    def _write_file(self, name: str, dir_destination: str):
        path = os.path.join(dir_destination, f"{name}.png")
        self._video.video.save_frame(path, t=self._frame_second)
