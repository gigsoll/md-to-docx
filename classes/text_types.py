from dataclasses import dataclass


@dataclass
class Text:
    text: str
    type: str = "plain"


@dataclass(kw_only=True)
class Hyprlink(Text):
    reference_number: int
    reference: str
    type: str = "hyprlink"
