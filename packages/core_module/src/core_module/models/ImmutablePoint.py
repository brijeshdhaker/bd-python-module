from dataclasses import dataclass, field

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

point = ImmutablePoint(10, 20)
# point.x = 15 -> This will raise a FrozenInstanceError