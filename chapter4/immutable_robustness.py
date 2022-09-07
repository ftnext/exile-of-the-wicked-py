from __future__ import annotations

import time
from dataclasses import dataclass
from threading import Thread
from typing import ClassVar, Final


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


@dataclass(frozen=True)
class Weapon:
    attack_power: AttackPower

    def reinforce(self, increment: AttackPower):
        """武器を強化する"""
        reinforced: Final[AttackPower] = attack_power.reinforce(increment)
        return self.__class__(reinforced)


# 別名参照問題は解決されている
attack_power: Final[AttackPower] = AttackPower(20)

weapon_a: Final[Weapon] = Weapon(attack_power)
weapon_b: Final[Weapon] = Weapon(attack_power)

increment: Final[AttackPower] = AttackPower(5)
reinforced_weapon_a: Final[Weapon] = weapon_a.reinforce(increment)

assert weapon_a.attack_power.value == weapon_b.attack_power.value == 20
assert reinforced_weapon_a.attack_power.value == 25


# スレッド間で使い回しても問題なし
def reinforce_worker(attack_power: AttackPower) -> None:
    print("reinforce_worker: start")
    print(f"reinforce_worker: {attack_power.value=}")
    print("reinforce_worker: REINFORCE!!")
    attack_power.reinforce(AttackPower(15))
    print(f"reinforce_worker: {attack_power.value=}")
    time.sleep(2)
    print("reinforce_worker: end")


def disable_worker(attack_power: AttackPower) -> None:
    print("disable_worker: start")
    time.sleep(1)
    print(f"disable_worker: {attack_power.value=}")
    print("disable_worker: DISABLE!!")
    attack_power.disable()
    print(f"disable_worker: {attack_power.value=}")
    print("disable_worker: end")


attack_power2 = AttackPower(20)

reinforce_thread = Thread(target=reinforce_worker, args=(attack_power2,))
disable_thread = Thread(target=disable_worker, args=(attack_power2,))

reinforce_thread.start()
disable_thread.start()
reinforce_thread.join()
disable_thread.join()

assert attack_power2.value == 20
