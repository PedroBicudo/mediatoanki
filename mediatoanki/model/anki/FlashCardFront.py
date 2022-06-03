class FlashCardFront:

    html: str = (
        "<div>{{ID}}</div>"
        "<div>{{SOUND}}</div>"
        "<div class=\"snapshot\">{{SNAPSHOT}}</div>"
    )

    def __init__(self, html: str = None):
        if html is not None:
            self.html = html
