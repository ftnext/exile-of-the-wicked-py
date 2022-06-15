from __future__ import annotations

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class Money:
    """
    >>> Money(100)
    Money(amount=100)

    >>> Money(-200)
    Traceback (most recent call last):
      ...
    ValueError: 金額が0以上でありません。

    >>> money = Money(1)
    >>> money.amount = 10000
    Traceback (most recent call last):
      ...
    dataclasses.FrozenInstanceError: cannot assign to field 'amount'
    >>> setattr(money, "amount", 10000)
    Traceback (most recent call last):
      ...
    dataclasses.FrozenInstanceError: cannot assign to field 'amount'
    >>> # @dataclass に slots=True を指定しなくても変更できない
    >>> money.spam = 42
    Traceback (most recent call last):
      ...
    dataclasses.FrozenInstanceError: cannot assign to field 'spam'

    >>> Money(100) + Money(200)
    Money(amount=300)
    >>> Money(100) + 200
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'Money' and 'int'
    """

    amount: Final[int]

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("金額が0以上でありません。")

    def __add__(self, other: Money) -> Money:
        if not isinstance(other, Money):
            return NotImplemented
        added = self.amount + other.amount
        return self.__class__(added)
