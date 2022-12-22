from random import randint

from Exceptions import GameOver, EnemyDown
from Settings import INITIAL_PLAYER_HEALTH, INITIAL_PLAYER_SCORE


class Enemy:
    def __init__(self, lvl: int):
        self.lvl = lvl
        self.health = lvl

    def decrease_health(self):
        if self.health == 1:
            raise EnemyDown
        self.health -= 1

    @staticmethod
    def random_choice():
        return randint(1, 3)


class Player:
    def __init__(self, name: str):
        self.name = name
        self.health = INITIAL_PLAYER_HEALTH
        self.score = INITIAL_PLAYER_SCORE

    def decrease_health(self):
        if self.health == 1:
            raise GameOver
        self.health -= 1

    @staticmethod
    def select_choice():
        check = ['1', '2', '3']
        while True:
            choice = input("MAKE A FIGHT CHOICE FROM (WARRIOR - 1, ROBBER - 2, WIZARD - 3: ")
            if choice not in check:
                continue
            return int(choice)

    @staticmethod
    def fight(attack: int, defence: int):
        # 1 Warrior beats 2 Robber
        # 2 Robber beats 3 Wizard
        # 3 Wizard beats 1 Warrior

        if attack == defence:
            return 1
        if attack == 1 and defence == 2:
            return 2
        if attack == 2 and defence == 3:
            return 2
        if attack == 3 and defence == 1:
            return 2
        else:
            return 3

    def attack(self, enemy_obj: Enemy):
        result = {1: "IT'S A DRAW!",
                  2: enemy_obj.decrease_health,
                  3: "YOUR ATTACK IS FAILED!"}
        attack = self.select_choice()
        defense = enemy_obj.random_choice()
        fight = self.fight(attack, defense)
        if fight == 2:
            print("YOUR ATTACK IS SUCCESSFUL!")
            self.score += 1
            return result[fight]()
        print(result[fight])

    def defense(self, enemy_obj: Enemy):
        result = {1: "IT'S A DRAW!",
                  2: "YOUR DEFENSE IS SUCCESSFUL!",
                  3: self.decrease_health}
        attack = self.select_choice()
        defense = enemy_obj.random_choice()
        fight = self.fight(attack, defense)
        if fight == 3:
            print("YOUR DEFENSE HAS BEEN BREACHED!")
            return result[fight]()
        print(result[fight])
