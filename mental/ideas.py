"""Idea hierarchy - from abstract to software-specific ideas."""

from mental.thoughts import Thought


class Idea(Thought):
    """A creative or generative thought."""

    description: str = "Idea"


class CreativeIdea(Idea):
    """An idea involving creation of something new."""

    description: str = "Creative idea"


class ProjectIdea(CreativeIdea):
    """An idea that could become an organized project."""

    description: str = "Project idea"


class SoftwareProjectIdea(ProjectIdea):
    """
    An idea for a software project.

    Can be marked as meta-circular (is_meta=True) when the idea
    is about creating the system that contains it.
    """

    description: str = "Software project idea"

    def __init__(self, content: str, language: str, is_meta: bool = False) -> None:
        super().__init__(content=content)
        self.language: str = language
        self.is_meta: bool = is_meta
