import os
from argparse import Namespace

from src.AnkiDeckGenerator import AnkiDeckGenerator
from src.SubtitleAudioCutter import SubtitleAudioCutter
from src.SubtitleFrameExtractor import SubtitleFrameExtractor
from src.SubtitleParser import SubtitleParser
from src.model.file.Video import Video


class MediaToAnkiArgParser:

    def __init__(self, args: Namespace):
        self._set_required_args(args)
        self._set_non_required_args(args)
        self._subtitles = []

    def run(self):
        self._generate_subs_with_pad()
        self._extract_frames_for_each_scene_of_subtitles()
        self._extract_audio_for_each_scene_of_subtitles()
        self._create_dir_to_store_deck_and_media()
        self._write_audio_and_frames_into_media_dir()
        self._create_anki_deck()

    def _generate_subs_with_pad(self):
        subparser = SubtitleParser()
        self._subtitles = subparser.get_subtitles_from_file(self._subtitle_source)
        self._update_pad_from_subs()

    def _create_dir_to_store_deck_and_media(self):
        try:
            print("Creating dirs...", end="")
            self._create_deck_and_media_dir()
            print("Done.")

        except Exception as error:
            print("Failed")
            raise

    def _create_deck_and_media_dir(self):
        self._deck_dir = os.path.join(self._destination, self._video.name.upper())
        self._deck_media_dir = os.path.join(self._deck_dir, "media")
        os.makedirs(self._deck_dir, exist_ok=True)
        os.makedirs(self._deck_media_dir, exist_ok=True)

    def _extract_frames_for_each_scene_of_subtitles(self):
        frame_extractor = SubtitleFrameExtractor(self._video)
        self._subtitles = frame_extractor.get_subtitles_with_one_frame_representing_each_subtitle(self._subtitles)

    def _extract_audio_for_each_scene_of_subtitles(self):
        audio_cutter = SubtitleAudioCutter(self._video)
        self._subtitles = audio_cutter.get_subtitles_with_one_audio_representing_the_subtitle_scene(self._subtitles)

    def _create_anki_deck(self):
        deck_gen = AnkiDeckGenerator(self._deck_dir, self._video.name.upper())
        deck_gen.generate_deck_based_on(self._subtitles)

    def _write_audio_and_frames_into_media_dir(self):
        for subtitle in self._subtitles:
            print(f"[SCENE ID] {subtitle.subtitle_id}")
            self._write_frame_from_subtitle_into_media_dir(subtitle)
            self._write_audio_from_subtitle_into_media_dir(subtitle)

    def _write_frame_from_subtitle_into_media_dir(self, subtitle):
        subtitle.frame.write_at(f"{subtitle.subtitle_id}", self._deck_media_dir)

    def _write_audio_from_subtitle_into_media_dir(self, subtitle):
        subtitle.audio.write_at(f"{subtitle.subtitle_id}", self._deck_media_dir)

    def _update_pad_from_subs(self):
        for subtitle in self._subtitles:
            subtitle.add_pad_start(self._padstart)
            subtitle.add_pad_end(self._padend)

    def _set_required_args(self, args: Namespace):
        if not MediaToAnkiArgParser._is_required_arguments_valid(args):
            raise

        self._destination = args.destination
        self._video = Video(args.video_source)
        self._subtitle_source = args.subtitle_source

    def _set_non_required_args(self, args: Namespace):
        self._padstart = args.padstart
        self._padend = args.padend

    @staticmethod
    def _is_required_arguments_valid(args: Namespace):
        return (
            MediaToAnkiArgParser._is_destination_valid(args.destination) and
            MediaToAnkiArgParser._is_video_valid(args.video_source) and
            MediaToAnkiArgParser._is_subtitle_valid(args.subtitle_source)
        )

    @staticmethod
    def _is_destination_valid(destination: str):
        return os.path.exists(destination) and os.path.isdir(destination)

    @staticmethod
    def _is_video_valid(video_path: str):
        return MediaToAnkiArgParser._is_file_valid(video_path)

    @staticmethod
    def _is_subtitle_valid(subtitle_path):
        return MediaToAnkiArgParser._is_file_valid(subtitle_path)

    @staticmethod
    def _is_file_valid(filepath):
        return os.path.exists(filepath) and os.path.isfile(filepath)
