"""Coding activities - software development."""

from typing import Optional
from activities.creative import CreativeActivity


class Coding(CreativeActivity):
    """Software development activity."""

    description: str = "Coding"

    def __init__(self, language: Optional[str] = None) -> None:
        self.language: Optional[str] = language
