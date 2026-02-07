"""Major categories of entities - second layer of abstraction."""

from core.entity import Entity


class MentalConstruct(Entity):
    """Things that exist in consciousness."""

    description: str = "Mental construct"


class Activity(Entity):
    """Things that are done, actions performed."""

    description: str = "Activity"


class Artifact(Entity):
    """Things that are created or exist as products."""

    description: str = "Artifact"


class Agent(Entity):
    """Entities with agency - capability to act and think."""

    description: str = "Agent"
