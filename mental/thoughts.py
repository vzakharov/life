"""Thought - any mental content."""

from core.categories import MentalConstruct


class Thought(MentalConstruct):
    """
    Any mental content.

    Thoughts exist independently - they are not "owned" by thinkers.
    People relate to thoughts via modalities (about, that, etc.).
    """

    description: str = "Thought"

    def __init__(self, content: str) -> None:
        self.content: str = content
