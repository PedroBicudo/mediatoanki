import os


class VideoPathUtils:

    @staticmethod
    def is_video_valid(video_path: str) -> bool:
        return (
                VideoPathUtils.__exists(video_path) and
                VideoPathUtils.__is_path_a_file(video_path) and
                VideoPathUtils.__is_file_a_video(video_path)
        )

    @staticmethod
    def __exists(video_path: str) -> bool:
        return os.path.exists(video_path)

    @staticmethod
    def __is_path_a_file(video_path: str) -> bool:
        return os.path.isfile(video_path)

    # TODO - Dar um jeito de saber se o arquivo é um vídeo.
    @staticmethod
    def __is_file_a_video(video_path: str) -> bool:
        return True
