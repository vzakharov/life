"""Project hierarchy - from abstract concepts to software projects."""

from typing import Optional
from core.categories import Artifact


class Concept(Artifact):
    """Abstract artifact - a structured idea."""

    description: str = "Concept"

    def __init__(self, name: str, description: Optional[str] = None) -> None:
        self.name: str = name
        self.concept_description: Optional[str] = description


class Plan(Concept):
    """Structured future-oriented concept."""

    description: str = "Plan"


class Project(Plan):
    """Organized effort with goals and timeline."""

    description: str = "Project"

    def __init__(self, name: str, description: Optional[str] = None, status: str = "planned") -> None:
        super().__init__(name=name, description=description)
        self.status: str = status


class CreativeProject(Project):
    """Project focused on creating something."""

    description: str = "Creative project"


class SoftwareProject(CreativeProject):
    """Project producing software."""

    description: str = "Software project"

    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        status: str = "planned",
        language: Optional[str] = None,
    ) -> None:
        super().__init__(name=name, description=description, status=status)
        self.language: Optional[str] = language
