from enum import Enum

class TextType(Enum):
    NORMAL = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, text_type, link=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.link = link

    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.link == value.link

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.link})"