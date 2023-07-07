<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from objects.Battle import Battle
from objects.Character import Character
from objects.Alignment import Alignment
<<<<<<< HEAD
=======
from objects.Battle import Battle
from objects.Character import Character
>>>>>>> 5ffa0be (add battle start messages)
=======
>>>>>>> 26062a9 (Create battle object, add battle messaging)

entities: list = []

def main():
    # #TODO create a character
    player = Character('Jason', 100, 20, 1)
    entities.append(player)
    # #TODO test that default alignment works
    # #TODO test that eplicit alignment works

    # #TODO create an enemy
<<<<<<< HEAD
<<<<<<< HEAD
    enemy = Character('Demon', 20, 5, alignment=2)
    entities.append(enemy)

    #TODO start a battle with character vs. enemy
    battle = Battle()


if __name__ == '__main__':
=======
=======
from objects.Arena import Arena

entities: list = []

>>>>>>> cf67462 (arena: add Arena and props, add gitignore)
def main():
    arena = Arena(entities)


if __name__ == '__main__':
>>>>>>> 91fc40b (arena: create main.py and Arena class)
=======
    enemy = Character()
=======
    enemy = Character('Demon', 20, 5, alignment=2)
>>>>>>> 26062a9 (Create battle object, add battle messaging)
    entities.append(enemy)

    #TODO start a battle with character vs. enemy
    battle = Battle()


if __name__ == '__main__':
>>>>>>> 5ffa0be (add battle start messages)
    main()