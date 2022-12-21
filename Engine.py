from Exceptions import EnemyDown, GameOver
from Models import Player, Enemy
from Settings import INITIAL_ENEMY_LEVEL


def get_player_name():
    while True:
        name = input("Choose your name: ")
        if len(name) < 1 or name.isspace():
            continue
        break
    return name.rstrip().strip()


def play():
    lvlup = 0
    player = Player(get_player_name())
    enemy = Enemy(INITIAL_ENEMY_LEVEL)
    while True:
        try:
            player.attack(enemy)
            player.defense(enemy)
        except EnemyDown:
            print(f"Enemy level {enemy.lvl} is defeated")
            enemy = Enemy(INITIAL_ENEMY_LEVEL + lvlup)
            player.score += 2
            lvlup += 1
            continue
        except KeyboardInterrupt:
            print(f'\nGame finished\nPlayer {player.name} has {player.score} score')
            break
        except GameOver:
            print(f"Game over! Player {player.name} has {player.score} score")
            with open('scores.txt', 'a') as file:
                file.write(f"Name: {player.name} --- points: {player.score}\n")
            break


play()
