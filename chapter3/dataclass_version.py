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
    """

    amount: Final[int]

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("金額が0以上でありません。")
