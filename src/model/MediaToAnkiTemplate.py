import genanki


class MediaToAnkiTemplate:
    def __init__(self):
        self._model = genanki.Model(
            model_id=1981874852,
            name="mediaToAnki",
            fields=MediaToAnkiTemplate._get_fields(),
            templates=MediaToAnkiTemplate._get_templates(),
            css=MediaToAnkiTemplate._get_css()
        )

    @property
    def model(self):
        return self._model

    @staticmethod
    def _get_fields():
        return [
            {'name': 'ID'},
            {'name': 'SOUND'},
            {'name': 'SNAPSHOT'},
            {'name': 'EXPRESSION'},
            {'name': 'PHONETIC'},
            {'name': 'MEANING'},
            {'name': 'WORD'},
            {'name': 'TRANSLATION'}
        ]

    @staticmethod
    def _get_templates():
        return [
            {
                "name": "mediatoankidefault",
                "qfmt": (
                    "<div>{{ID}}</div>"
                    "<div>{{SOUND}}</div>"
                    "<div class=\"snapshot\">{{SNAPSHOT}}</div>"
                ),

                "afmt": (
                        "{{FrontSide}}<br>"
                        "<hr id=answer><br>"
                        "<div class=\"expression\">{{EXPRESSION}}</div><br>"
                        "<div class=\"phonetic\">{{PHONETIC}}</div>"
                        "<div>{{WORD}} <span class=\"translation\">{{TRANSLATION}}</span></div>"
                        "<div class=\"meaning\">{{MEANING}}</div>"
                )
            }
        ]

    @staticmethod
    def _get_css():
        return (
            ".card {font-family: arial;font-size:20px;text-align:center;color:black;background-color:white;}"
            "div.snapshot {display: inline-block;width: 500px;height: auto;}"
            "div > img {width: 100%; height: auto;}"
            "div.phonetic {font-weight: bold;}"
            "span.translation {font-weight: bold;}"
    )