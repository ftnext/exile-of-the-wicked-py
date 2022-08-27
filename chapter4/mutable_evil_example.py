import time
from dataclasses import dataclass
from threading import Thread
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


# スレッド間での使い回しの例
def reinforce_worker(attack_power: AttackPower) -> None:
    print("reinforce_worker: start")
    print(f"reinforce_worker: {attack_power.value=}")
    print("reinforce_worker: REINFORCE!!")
    attack_power.reinforce(15)
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


attack_power = AttackPower(20)

reinforce_thread = Thread(target=reinforce_worker, args=(attack_power,))
disable_thread = Thread(target=disable_worker, args=(attack_power,))

reinforce_thread.start()
disable_thread.start()
reinforce_thread.join()
disable_thread.join()

assert attack_power.value == 0

"""
reinforce_worker: start
reinforce_worker: attack_power.value=20
reinforce_worker: REINFORCE!!
reinforce_worker: attack_power.value=35
disable_worker: start
disable_worker: attack_power.value=35
disable_worker: DISABLE!!
disable_worker: attack_power.value=0
disable_worker: end
reinforce_worker: end
"""
