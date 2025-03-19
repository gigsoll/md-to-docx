from dataclasses import dataclass
from classes.text_types import Text


@dataclass
class PlainLine:
    content: list[Text]


@dataclass
class OrderedListMember(PlainLine):
    order_number: int
    nesting_level: int = 0


@dataclass
class UnorderedListMember(PlainLine):
    nesting_level: int = 0


@dataclass
class CodeBlockMember(PlainLine):
    language: str
    line_number: int


@dataclass
class Header(PlainLine):
    nesting_level: int = 1


@dataclass
class Image(PlainLine):
    source: str
    caption: str
