from dataclasses import dataclass
from typing import Final


class Member:
    """DamageLogicで再代入しないコードを書くための仮実装。サンプルファイル参照"""

    def power(self) -> int:
        return 10

    def weapon_attack(self) -> int:
        return 20

    def speed(self) -> int:
        return 10


@dataclass
class Enemy:
    defence: int


@dataclass
class DamageLogic:
    """
    >>> damage_logic = DamageLogic(Member(), Enemy(25))
    >>> damage_logic.damage()  # final_attack_power: 33, reduction: 12
    21
    """

    member: Member
    enemy: Enemy

    def damage(self) -> int:
        basic_attack_power: Final[int] = (
            self.member.power() + self.member.weapon_attack()
        )
        final_attack_power: Final[int] = int(
            basic_attack_power * (1 + self.member.speed() / 100)
        )
        reduction: Final[int] = int(self.enemy.defence / 2)
        damage: Final[int] = max(0, final_attack_power - reduction)

        return damage
