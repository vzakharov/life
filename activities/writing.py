"""Writing activities - textual creation."""

from typing import Optional
from activities.creative import CreativeActivity


class Writing(CreativeActivity):
    """Textual creative activity."""

    description: str = "Writing"


class Journaling(Writing):
    """
    Reflective writing about experiences.

    Can be instantiated with specific mediums (code, text, etc.).
    """

    description: str = "Journaling"

    def __init__(self, medium: Optional[str] = None, language: Optional[str] = None) -> None:
        self.medium: Optional[str] = medium
        self.language: Optional[str] = language


# Global instance for code journaling
CODE_JOURNALING: Journaling = Journaling(medium="code", language="python")
