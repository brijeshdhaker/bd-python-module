
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1  # Default value
    # Hides internal ID from print statements
    internal_id: str = field(default="0000", repr=False)
    # Correct way to assign a default empty list
    tags: list[str] = field(default_factory=list) 