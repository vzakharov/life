"""Root abstraction for all entities in the life journaling system."""

from abc import ABC


class Entity(ABC):
    """
    Base class for everything in the system.

    All entities (thoughts, activities, artifacts, agents) inherit from this.
    Minimal and clean - no database-like features.
    """

    description: str = ""
