import unittest

from mediatoanki.model.anki.FlashCardFieldsContent import \
    FlashCardFieldsContent


class FlashCardFieldsContentTestCase(unittest.TestCase):

    def test_html_content_is_equal_to_expected(self):
        # Given
        content = FlashCardFieldsContent("1", "text")

        # When
        html = content.html

        # Then
        expected = [
            "1",
            "[sound:1.mp3]",
            "<img src=\"1.png\">",
            "text"
            "", "", "", "", ""
        ]
        self.assertListEqual(
            expected, html,
            msg="Check if the correct HTML is generated"
        )

    def test_html_content_is_equal_when_attribute_is_modified(self):
        # Given
        content = FlashCardFieldsContent("1", "text")

        # When
        content.subtitle_id = 2
        content.subtitle_text = "foo"
        html = content.html

        # Then
        expected = [
            "2",
            "[sound:2.mp3]",
            "<img src=\"2.png\">",
            "foo"
            "", "", "", "", ""
        ]
        self.assertListEqual(
            expected, html,
            msg=(
                "Check if the correct HTML is generated "
                "when attribute values are changed"
            )
        )


if __name__ == '__main__':
    unittest.main()
