"""Subjects - what things are about."""

from core.entity import Entity


class Subject(Entity):
    """What something is about."""

    description: str = "Subject"

    def __init__(self, name: str) -> None:
        self.name: str = name


class Life(Subject):
    """
    The totality of one's existence and experiences.

    Meta-subject - life containing itself.
    """

    description: str = "Life itself"

    def __init__(self) -> None:
        super().__init__(name="life")
