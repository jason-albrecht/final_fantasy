from objects.Battle import Battle
from objects.Character import Character

entities: list = []

def main():
    # #TODO create a character
    player = Character('Jason', 100, 20, 1)
    entities.append(player)
    # #TODO test that default alignment works
    # #TODO test that eplicit alignment works

    # #TODO create an enemy
    enemy = Character()
    entities.append(enemy)

    #TODO start a battle with character vs. enemy
    battle = Battle(entities)


if __name__ == '__main__':
    main()