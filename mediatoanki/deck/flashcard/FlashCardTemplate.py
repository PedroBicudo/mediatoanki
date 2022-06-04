from typing import Dict, List

import genanki

from mediatoanki.model.anki.FlashCardBack import FlashCardBack
from mediatoanki.model.anki.FlashCardCSS import FlashCardCSS
from mediatoanki.model.anki.FlashCardFront import FlashCardFront


class FlashCardTemplate:

    ID: int = 1981874852
    name: str = "mediatoankidefault"
    fields: List[Dict[str, str]] = [
            {'name': 'ID'},
            {'name': 'SOUND'},
            {'name': 'SNAPSHOT'},
            {'name': 'EXPRESSION'},
            {'name': 'PHONETIC'},
            {'name': 'MEANING'},
            {'name': 'WORD'},
            {'name': 'TRANSLATION'}
    ]
    front: FlashCardFront = FlashCardFront()
    back: FlashCardBack = FlashCardBack()
    css: FlashCardCSS = FlashCardCSS()
    _model: genanki.Model = None

    def __int__(
            self,
            name: str = None,
            fields: List[Dict[str, str]] = None,
            front: FlashCardFront = None,
            back: FlashCardBack = None,
            css: FlashCardCSS = None
    ):
        if name is not None:
            self.name = name
        if fields is not None:
            self.fields = fields
        if front is not None:
            self.front = front
        if back is not None:
            self.back = back
        if css is not None:
            self.css = css

    @property
    def model(self) -> genanki.Model:
        if self._model is None:
            self._model = genanki.Model(
                model_id=self.ID,
                name="mediaToAnki",
                fields=self.fields,
                templates=[{
                    'name': self.name,
                    'qfmt': self.front.html,
                    'afmt': self.back.html
                }],
                css=self.css.css
            )

        return self._model
