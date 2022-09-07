from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class AttackPower:
    """
    >>> attack_power = AttackPower(20)
    >>> reinforced = attack_power.reinforce(AttackPower(15))
    >>> print(f"attack power: {attack_power.value=} {reinforced.value=}")
    attack power: attack_power.value=20 reinforced.value=35
    """

    MIN: ClassVar[int] = 0
    value: int

    def __post_init__(self):
        if self.value < self.MIN:
            raise ValueError(f"{self.MIN}以上を指定してください")

    def reinforce(self, increment: AttackPower):
        """攻撃力を強化する"""
        return self.__class__(self.value + increment.value)

    def disable(self):
        """無力化する"""
        return self.__class__(self.MIN)
