from dataclasses import dataclass
from typing import ClassVar, Final


@dataclass
class HitPoint:
    """
    >>> hit_point = HitPoint(20)
    >>> hit_point.damage(15)
    >>> hit_point.amount
    5
    >>> hit_point.is_zero()
    False
    >>> hit_point.damage(10)
    >>> hit_point.amount
    0
    >>> hit_point.is_zero()
    True
    """

    MIN: ClassVar[int] = 0
    amount: int

    def __post_init__(self):
        if self.amount < self.MIN:
            raise ValueError(f"{self.MIN}以上を指定してください")

    def damage(self, damage_amount: int) -> None:
        next_amount: Final[int] = self.amount - damage_amount
        self.amount = max(self.MIN, next_amount)

    def is_zero(self) -> bool:
        return self.amount == self.MIN
