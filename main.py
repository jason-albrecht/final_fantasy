<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 826dcc5 (arena: add Arena and props, add gitignore)
=======
>>>>>>> d0cc235 (make arena an object)
from objects.Battle import Battle
from objects.Character import Character
<<<<<<< HEAD
from objects.Alignment import Alignment
<<<<<<< HEAD
<<<<<<< HEAD
=======
from objects.Battle import Battle
from objects.Character import Character
>>>>>>> 5ffa0be (add battle start messages)
=======
>>>>>>> 26062a9 (Create battle object, add battle messaging)
=======
=======
>>>>>>> 5ffa0be (add battle start messages)
>>>>>>> bc66dd4 (add battle start messages)

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
=======
>>>>>>> bc66dd4 (add battle start messages)
<<<<<<< HEAD
    enemy = Character('Demon', 20, 5, alignment=2)
    entities.append(enemy)

    #TODO start a battle with character vs. enemy
    battle = Battle()
=======
    enemy = Character()
    entities.append(enemy)

    #TODO start a battle with character vs. enemy
    battle = Battle(entities)
>>>>>>> 5ffa0be (add battle start messages)


if __name__ == '__main__':
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 826dcc5 (arena: add Arena and props, add gitignore)
from objects.Arena import Arena

entities: list = []

<<<<<<< HEAD
>>>>>>> cf67462 (arena: add Arena and props, add gitignore)
=======
>>>>>>> 826dcc5 (arena: add Arena and props, add gitignore)
def main():
    arena = Arena(entities)


if __name__ == '__main__':
<<<<<<< HEAD
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
=======
>>>>>>> cf67462 (arena: add Arena and props, add gitignore)
>>>>>>> 826dcc5 (arena: add Arena and props, add gitignore)
=======
>>>>>>> d0cc235 (make arena an object)
    main()