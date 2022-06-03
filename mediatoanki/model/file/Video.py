import os

from moviepy.video.io.VideoFileClip import VideoFileClip

from mediatoanki.utils.FileUtils import FileUtils


class Video:

    def __init__(self, video_path: str):
        self._set_video_path(video_path)
        self._name = os.path.basename(video_path)
        self._video = VideoFileClip(video_path)

    def _set_video_path(self, video_path: str):
        FileUtils.validate_video(video_path)
        self.__video_path = video_path

    @property
    def name(self) -> str:
        return ".".join(self._name.split(".")[:-1])

    @property
    def video(self) -> VideoFileClip:
        return self._video
