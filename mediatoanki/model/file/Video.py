import os

from moviepy.video.io.VideoFileClip import VideoFileClip

from mediatoanki.utils.VideoPathUtils import VideoPathUtils


class Video:

    def __init__(self, video_path: str):
        self._set_video_path(video_path)
        self._name = os.path.basename(video_path)
        self._video = VideoFileClip(video_path)

    def _set_video_path(self, video_path: str):
        if not VideoPathUtils.is_video_valid(video_path):
            raise

        self.__video_path = video_path

    @property
    def name(self) -> str:
        return ".".join(self._name.split(".")[:-1])

    @property
    def video(self) -> VideoFileClip:
        return self._video
