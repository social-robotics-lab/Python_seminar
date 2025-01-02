"""
練習問題クラス定義用ファイル
"""

import random as rnd
from typing import Dict, Optional, Tuple, Union, Literal


class Skill:
    def __init__(
        self,
        damage: int,
        self_damage: Optional[int] = None,
        self_healing: Optional[int] = None,
    ):
        self.damage = damage
        self.self_damage = self_damage
        self.self_healing = self_healing

class Character:
    def __init__(self, name: str) -> None:
        self.name = name
        self.is_dead = False

    def get_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.is_dead = True

class MainCharacterSkills:
    def __init__(self, base_damage: int,special_damage: int,self_damage: int,self_healing: int):
        self.base = Skill(damage=base_damage)
        self.special = Skill(damage=special_damage, self_damage=self_damage, self_healing=self_healing)

class MainCharacter(Character):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.hp, self.skills = self.__gain_abilities()

    def __gain_abilities(
        self,
    ) -> Tuple[int, Dict[str, MainCharacterSkills]]:
        hps = [150, 160, 170, 180, 190, 200]
        hp = rnd.choice(hps)
        base_damage = 25 if hp < 180 else 20
        special_damage = rnd.choice([50, 60, 70, 80])

        if hp >= 190:
            if special_damage >= 70:
                self_damage = 10
            else:
                self_damage = 5
            self_healing = 0
        else:
            self_damage = 0
            self_healing = 10

        skill = MainCharacterSkills(
            base_damage=base_damage,
            special_damage=special_damage,
            self_damage=self_damage,
            self_healing=self_healing,
        )
        return hp, skill

    def attack(self, type: Literal["base", "special"]) -> int:
        if type == "base":
            damage = self.skills.base.damage

        else:
            damage = self.skills.special.damage
            self.hp -= self.skills.special.self_damage
            self.hp += self.skills.special.self_healing
        return damage
    
        
class Enemy(Character):
    def __init__(self, name: str, difficulty: Literal["easy", "normal", "hard"], index: int):
        super().__init__(name=name)
        self.difficulty = difficulty
        self.index = index + 1
        self.hp, self.skill = self.__gain_abilities()
        
    def __gain_abilities(self) -> Tuple[int, Skill]:
        if self.difficulty == "easy":
            hp = 20 * self.index
        elif self.difficulty == "normal":
            hp = 40 * self.index
        else:
            hp = 60 * self.index

        skill = Skill(damage=hp // 6)
        return hp, skill
    
    def attack(self) -> int:
        return self.skill.damage