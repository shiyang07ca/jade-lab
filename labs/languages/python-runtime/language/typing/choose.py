import random
from typing import Sequence, TypeVar

Choosable = TypeVar("Choosable", str, float)


def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)


# reveal_type(choose(["Guido", "Jukka", "Ivan"]))
# reveal_type(choose([1, 2, 3]))
# reveal_type(choose([True, 42, 3.14]))
# reveal_type(choose(["Python", 3, 7]))
