"""Repository hierarchy - digital artifacts and codebases."""

from typing import Optional
from core.categories import Artifact


class DigitalArtifact(Artifact):
    """Artifacts existing in digital form."""

    description: str = "Digital artifact"


class Codebase(DigitalArtifact):
    """Collection of code files."""

    description: str = "Codebase"


class Repository(Codebase):
    """Version-controlled codebase."""

    description: str = "Repository"

    def __init__(self, name: str) -> None:
        self.name: str = name


class ProgrammingRepository(Repository):
    """Repository containing programming code."""

    description: str = "Programming repository"


class PythonRepository(ProgrammingRepository):
    """Repository primarily containing Python code."""

    description: str = "Python repository"
