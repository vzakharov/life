"""People - agents with the ability to think and relate to thoughts."""

from typing import Any
from core.categories import Agent


class Person(Agent):
    """
    A human being.

    People can engage with thoughts through different modalities
    using the thought() method with keyword arguments.
    """

    description: str = "Person"

    def __init__(self, name: str) -> None:
        self.name: str = name

    def thought(self, **modalities: Any) -> None:
        """
        Engage with thoughts via modalities.

        Modalities express different ways of relating to thoughts:
        - about: contemplation of something
        - that: belief or assertion
        - ... more modalities can emerge organically

        Examples:
            I.thought(about=GENESIS_IDEA)
            I.thought(that="life is beautiful")
            I.thought(about=LIFE, that="it sucks")
        """
        # For now, this is purely expressive
        # Future: could record these relationships
        pass


# The central self - the I that experiences and journals
I: Person = Person("Vova")
