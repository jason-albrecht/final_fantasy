from dataclasses import dataclass

@dataclass
class Arena:
    def __init__(self, entities: list) -> None:
        self._entities = entities

    def _get_entities(self):
        print("Get entities")
        return self._entities
    
    def _set_entities(self, new_entities: list) -> list:
        print("Set entities")
        self._entities = new_entities
        return new_entities
    
    def _del_entities(self) -> None:
        print("Delete entities")
        del self._entities

    entities = property(
        fget=_get_entities,
        fset=_set_entities,
        fdel=_del_entities,
        doc="The entities property."
    )