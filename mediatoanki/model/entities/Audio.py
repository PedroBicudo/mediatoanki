import os

from moviepy.audio.io.AudioFileClip import AudioFileClip

from mediatoanki.model.entities.File import File


class Audio(File):

    _audio: AudioFileClip

    def __init__(self, audio: AudioFileClip):
        self._audio: AudioFileClip = audio

    def write_at(self, name: str, dir_destination: str):
        print("\tSaving audio...", end="")
        try:
            self._write_file(name, dir_destination)
            print("Done")

        except Exception:
            print("Failed")

    def _write_file(self, name: str, dir_destination: str):
        path = os.path.join(dir_destination, f"{name}.mp3")
        self._audio.write_audiofile(path, logger=None)
