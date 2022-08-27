from dataclasses import dataclass
from typing import ClassVar


@dataclass
class AttackPower:
    MIN: ClassVar[int] = 0
    value: int

    def __post_init__(self):
        if self.value < self.MIN:
            raise ValueError(f"{self.MIN}以上を指定してください")

    def reinforce(self, increment: int) -> None:
        """攻撃力を強化する"""
        self.value += increment

    def disable(self):
        """無力化する"""
        self.value = self.MIN


@dataclass
class Weapon:
    attack_power: AttackPower


# 使い回しによる悪魔（別名参照問題）
attack_power = AttackPower(20)

weapon_a = Weapon(attack_power)
weapon_b = Weapon(attack_power)

weapon_a.attack_power.reinforce(5)

assert id(weapon_a.attack_power) == id(weapon_b.attack_power)
assert weapon_a.attack_power.value == weapon_b.attack_power.value == 25
