from dataclasses import dataclass, field
import logging
logging.basicConfig(level=logging.INFO)

@dataclass
class Battle():
    '''Start a battle'''

<<<<<<< HEAD
    _entities: list = field(default_factory=True)
    _team_count: int = field(default = 2, repr=False)
    _obj_type: str = field(default = 'battle', repr=False)
    _start_message: str = field(default='Battle started!', repr=False)

    def __init__(self, entities: list) -> None:
        print(Battle._start_message)
        print(f"{entities[0]} vs. {entities[1]}")
=======
    entities = []
    team_count: int = field(default = 2, repr=False)
    _obj_type: str = field(default = 'battle', repr=False)
    _start_message: str = field(default='Battle started!', repr=False)

    def __post_init__(self, entities) -> None:
        print(Battle._start_message)
        print(f"{entities[0]} vs. {entities[1]}")
    # print(_start_message)

# entities: list = [1, 2]
# test = Battle(entities)
>>>>>>> 5ffa0be (add battle start messages)
