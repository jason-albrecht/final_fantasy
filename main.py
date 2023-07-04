from objects.Battle import Battle
from objects.Character import Character
from objects.Alignment import Alignment
from objects.Battle import Battle
from objects.Character import Character
from objects.Alignment import Alignment

entities: list = []

def main():
    # #TODO create a character
    player = Character('Jason', 100, 20, 1)
    entities.append(player)
    # #TODO test that default alignment works
    # #TODO test that eplicit alignment works

    # #TODO create an enemy
    enemy = Character('Demon', 20, 5, 2)
    entities.append(enemy)

    #TODO start a battle with character vs. enemy
    enemy = Character('Demon', 20, 5, alignment=2)
    entities.append(enemy)

    #TODO start a battle with character vs. enemy
    battle = Battle(entities)

if __name__ == '__main__':
    main()