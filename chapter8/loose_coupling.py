from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class RegularPrice:
    """
    >>> RegularPrice(350)
    RegularPrice(amount=350)
    >>> RegularPrice(-1)
    Traceback (most recent call last):
      ...
    ValueError: 価格が0以上でありません
    """

    MIN_AMOUNT: ClassVar[int] = 0
    amount: int

    def __post_init__(self) -> None:
        if self.amount < self.MIN_AMOUNT:
            raise ValueError("価格が0以上でありません")


@dataclass(frozen=True)
class RegularDiscountedPrice:
    """
    >>> RegularDiscountedPrice.from_price(RegularPrice(470))
    RegularDiscountedPrice(amount=70)
    >>> RegularDiscountedPrice.from_price(RegularPrice(350))
    RegularDiscountedPrice(amount=0)
    """

    MIN_AMOUNT: ClassVar[int] = 0
    DISCOUNT_AMOUNT: ClassVar[int] = 400
    amount: int

    @classmethod
    def from_price(cls, price: RegularPrice) -> RegularDiscountedPrice:
        discounted_amount = price.amount - cls.DISCOUNT_AMOUNT
        if discounted_amount < cls.MIN_AMOUNT:
            discounted_amount = cls.MIN_AMOUNT
        return cls(discounted_amount)


@dataclass(frozen=True)
class RegularDiscountedPriceV2:
    """イニシャライザにRegularPriceを渡せるバージョン

    >>> RegularDiscountedPriceV2(RegularPrice(470))
    RegularDiscountedPriceV2(amount=70)
    >>> RegularDiscountedPriceV2(RegularPrice(350))
    RegularDiscountedPriceV2(amount=0)
    """

    MIN_AMOUNT: ClassVar[int] = 0
    DISCOUNT_AMOUNT: ClassVar[int] = 400
    amount: int

    def __init__(self, price: RegularPrice) -> None:
        discounted_amount = price.amount - self.DISCOUNT_AMOUNT
        if discounted_amount < self.MIN_AMOUNT:
            discounted_amount = self.MIN_AMOUNT
        object.__setattr__(self, "amount", discounted_amount)


@dataclass(frozen=True)
class SummerDiscountedPrice:
    """
    >>> SummerDiscountedPrice.from_price(RegularPrice(350))
    SummerDiscountedPrice(amount=50)
    >>> SummerDiscountedPrice.from_price(RegularPrice(230))
    SummerDiscountedPrice(amount=0)
    """

    MIN_AMOUNT: ClassVar[int] = 0
    DISCOUNT_AMOUNT: ClassVar[int] = 300
    amount: int

    @classmethod
    def from_price(cls, price: RegularPrice) -> SummerDiscountedPrice:
        discounted_amount = price.amount - cls.DISCOUNT_AMOUNT
        if discounted_amount < cls.MIN_AMOUNT:
            discounted_amount = cls.MIN_AMOUNT
        return cls(discounted_amount)
