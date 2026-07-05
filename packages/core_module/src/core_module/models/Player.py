
#

from dataclasses import dataclass, field

@dataclass(order=True)
class Player:
    score: int   # First field checked during sorting
    name: str


p1 = Player(90, "Alice")
p2 = Player(95, "Bob")
print(p1 < p2)  # Output: True