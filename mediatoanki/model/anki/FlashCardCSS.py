class FlashCardCSS:
    css: str = (
        ".card {"
        "font-family: arial;"
        "font-size:20px;"
        "text-align:center;"
        "color:black;"
        "background-color:white;"
        "}"
        "div.snapshot {"
        "display: inline-block;"
        "width: 500px;"
        "height: auto;"
        "}"
        "div > img {"
        "width: 100%; "
        "height: auto;"
        "}"
        "div.phonetic {"
        "font-weight: bold;"
        "}"
        "span.translation {"
        "font-weight: bold;"
        "}"
    )

    def __init__(self, css: str = None):
        if css is not None:
            self.css = css
