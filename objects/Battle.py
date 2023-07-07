from dataclasses import dataclass, field
import logging
logging.basicConfig(level=logging.INFO)

@dataclass
class Battle():
    '''Start a battle'''

    _entities: list = field(default_factory=True)
    _team_count: int = field(default = 2, repr=False)
    _obj_type: str = field(default = 'battle', repr=False)
    _start_message: str = field(default='Battle started!', repr=False)

    def __init__(self, entities) -> None:
        print(Battle._start_message)
        print(f"{entities[0].name} vs. {entities[1].name}")
    # print(_start_message)

# entities: list = [1, 2]
# test = Battle(entities)
