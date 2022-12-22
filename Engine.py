from Exceptions import EnemyDown, GameOver
from Models import Player, Enemy
from Settings import INITIAL_ENEMY_LEVEL


def get_player_name() -> str:
    name: str = ""
    while not name:
        name = input("Choose your name: ").strip()
    return name


def write_to_file(player: Player) -> None:
    with open('scores.txt', 'a') as file:
        file.write(f"Name: {player.name} --- points: {player.score}\n")


def play():
    lvlup = INITIAL_ENEMY_LEVEL
    player = Player(get_player_name())
    enemy = Enemy(INITIAL_ENEMY_LEVEL)
    while True:
        try:
            player.attack(enemy)
            player.defense(enemy)
        except EnemyDown:
            print(f"Enemy level {enemy.lvl} is defeated")
            lvlup += 1
            enemy = Enemy(lvlup)
            player.score += 2
            continue
        except KeyboardInterrupt:
            print(f'\nGame finished\nPlayer {player.name} has {player.score} score')
            write_to_file(player)
            break
        except GameOver:
            print(f"Game over! Player {player.name} has {player.score} score")
            write_to_file(player)
            break


if __name__ == "__main__":
    play()
