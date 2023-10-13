from __future__ import annotations

from dataclasses import dataclass
from typing import NoReturn


class MoneyValueDescriptor:
    def __get__(self, obj, type=None) -> int:
        return obj.__value

    def __set__(self, obj, value: int) -> None:
        if value < 0:
            raise ValueError("金額が0以上でありません。")
        if hasattr(obj, f"_{self.__class__.__name__}__value"):
            raise AttributeError("Cannot set this attribute")
        obj.__value = value

    def __delete__(self, obj) -> NoReturn:
        raise AttributeError("Cannot delete this attribute")


@dataclass
class Money:
    """
    >>> Money(100, "¥")
    Money(amount=100, currency='¥')

    >>> Money(-200, "¥")
    Traceback (most recent call last):
      ...
    ValueError: 金額が0以上でありません。

    >>> money = Money(1, "¥")
    >>> money.amount
    1
    >>> money.amount = 10000
    Traceback (most recent call last):
      ...
    AttributeError: Cannot set this attribute
    >>> setattr(money, "amount", 10000)
    Traceback (most recent call last):
      ...
    AttributeError: Cannot set this attribute
    >>> object.__setattr__(money, "amount", 20000)
    Traceback (most recent call last):
      ...
    AttributeError: Cannot set this attribute

    >>> money.spam = 42
    >>> money.spam
    42

    >>> Money(100, "¥") + Money(200, "¥")
    Money(amount=300, currency='¥')
    >>> Money(100, "¥") + 200
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'Money' and 'int'
    >>> Money(100, "¥") + Money(200, "$")
    Traceback (most recent call last):
      ...
    ValueError: 通貨単位が違います。

    >>> Money(100, "¥") == Money(100, "¥")
    True
    >>> Money(100, "¥") == Money(100, "$")
    False
    """

    amount = MoneyValueDescriptor()

    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(amount={self.amount}, currency={self.currency!r})"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __add__(self, other: Money) -> Money:
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("通貨単位が違います。")
        added = self.amount + other.amount
        return self.__class__(added, self.currency)
