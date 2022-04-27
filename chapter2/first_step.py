from __future__ import annotations

from typing import Final


class HitPoint:
    """ヒットポイント（HP）を表現するクラス"""

    MIN: Final[int] = 0
    MAX: Final[int] = 999

    def __init__(self, value: int) -> None:
        """
        >>> hp = HitPoint(100)

        >>> hp = HitPoint(0)
        >>> hp = HitPoint(-1)
        Traceback (most recent call last):
          ...
        ValueError: 0以上を指定してください

        >>> hp = HitPoint(999)
        >>> hp = HitPoint(1000)
        Traceback (most recent call last):
          ...
        ValueError: 999以下を指定してください
        """
        if value < self.MIN:
            raise ValueError(f"{self.MIN}以上を指定してください")
        if value > self.MAX:
            raise ValueError(f"{self.MAX}以下を指定してください")

        self.value = value

    def damage(self, damage_amount: int) -> HitPoint:
        """ダメージを受ける

        >>> HitPoint(100).damage(70)
        HitPoint(value=30)
        >>> HitPoint(100).damage(108)
        HitPoint(value=0)
        """
        damaged = self.value - damage_amount
        corrected = self.MIN if damaged < self.MIN else damaged
        return self.__class__(corrected)

    def recover(self, recovery_amount: int) -> HitPoint:
        """回復する

        >>> HitPoint(900).recover(70)
        HitPoint(value=970)
        >>> HitPoint(900).recover(108)
        HitPoint(value=999)
        """
        recovered = self.value + recovery_amount
        corrected = self.MAX if recovered > self.MAX else recovered
        return self.__class__(corrected)

    def __repr__(self) -> str:
        return f"HitPoint(value={self.value})"
