

from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str
    slug: str = field(init=False) # Excluded from __init__ arguments

    def __post_init__(self):
        self.slug = f"{self.title.lower().replace(' ', '-')}-by-{self.author.lower()}"