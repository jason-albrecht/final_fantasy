from dataclasses import dataclass
from objects.Alignment import Alignment

@dataclass
class Character:
    '''Create a character'''

    name: str
    hp: int
    mp: int
    alignment: Alignment