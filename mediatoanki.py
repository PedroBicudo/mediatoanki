import argparse

from src.MediaToAnkiArgParser import MediaToAnkiArgParser

parser = argparse.ArgumentParser(description="Create an anki deck given media and subtitles.")

parser.add_argument(
    "video_source",
    metavar="video_source",
    type=str,
    help="Video file (.mp4, .mkv)"
)
parser.add_argument(
    "subtitle_source",
    metavar="subtitle_source",
    type=str, help="Subtitle file (.vtt, .src, etc)"
)
parser.add_argument(
    "--padstart",
    metavar="seconds",
    type=int,
    default=0,
    help="Add more time to the start of the scene from subtitle"
)
parser.add_argument(
    "--padend",
    metavar="seconds",
    type=int,
    default=0,
    help="Add more time to the end of the scene from subtitle"
)
parser.add_argument(
    "destination",
    metavar="dest",
    type=str,
    help="Destination for files."
)

args = parser.parse_args()
media_to_anki = MediaToAnkiArgParser(args)
media_to_anki.run()

# TODO - Adicionar uma classe que vai organizar escrever os arquivos em outro diretório.
# TODO - Adicionar um argparse
# TODO - Adicionar um modo verboso
# TODO - Criar uma classe que vai lidar com a atualizacao padding
