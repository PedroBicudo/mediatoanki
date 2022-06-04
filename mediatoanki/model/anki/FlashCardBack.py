class FlashCardBack:
    html: str = (
        "{{FrontSide}}<br>"
        "<hr id=answer><br>"
        "<div class=\"expression\">{{EXPRESSION}}</div><br>"
        "<div class=\"phonetic\">{{PHONETIC}}</div>"
        "<div>{{WORD}} "
        "<span class=\"translation\">{{TRANSLATION}}</span>"
        "</div>"
        "<div class=\"meaning\">{{MEANING}}</div>"
    )

    def __init__(self, html: str = None):
        if html is not None:
            self.html = html
