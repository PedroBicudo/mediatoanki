from typing import List


class FlashCardFieldsContent:

    def __init__(self, subtitle_id: int, subtitle_text: str):
        self.subtitle_id = subtitle_id
        self.subtitle_text = subtitle_text

    @property
    def html(self) -> List[str]:
        return [
            f"{self.subtitle_id}",
            f"[sound:{self.subtitle_id}.mp3]",
            f"<img src=\"{self.subtitle_id}.png\">",
            f"{self.subtitle_text}"
            "", "", "", "", ""
        ]
