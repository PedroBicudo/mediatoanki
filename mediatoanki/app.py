import argparse
import sys

from mediatoanki.MediaToAnkiArgParser import MediaToAnkiArgParser

parser = argparse.ArgumentParser(
    description="Create an anki deck given media and subtitles."
)

parser.add_argument(
    "video_source",
    metavar="video_source",
    type=str,
    help="Video file (.mp4, .mkv)",
)
parser.add_argument(
    "subtitle_source",
    metavar="subtitle_source",
    type=str,
    help="Subtitle file (.vtt, .src, etc)",
)
parser.add_argument(
    "--padstart",
    metavar="seconds",
    type=int,
    default=0,
    help="Add more time to the start of the scene from subtitle",
)
parser.add_argument(
    "--padend",
    metavar="seconds",
    type=int,
    default=0,
    help="Add more time to the end of the scene from subtitle",
)
parser.add_argument(
    "destination", metavar="dest", type=str, help="Destination for files."
)


def main():
    try:
        args = parser.parse_args()
        media_to_anki = MediaToAnkiArgParser(args)
        media_to_anki.run()

    except OSError as e:
        print("System Error: "+str(e))
        sys.exit(-1)


if __name__ == "__main__":
    main()
