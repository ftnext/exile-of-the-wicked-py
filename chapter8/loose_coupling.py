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

    def __post_init__(self):
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
    def from_price(cls, price: RegularPrice):
        discounted_amount = price.amount - cls.DISCOUNT_AMOUNT
        if discounted_amount < cls.MIN_AMOUNT:
            discounted_amount = cls.MIN_AMOUNT
        return cls(discounted_amount)


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
    def from_price(cls, price: RegularPrice):
        discounted_amount = price.amount - cls.DISCOUNT_AMOUNT
        if discounted_amount < cls.MIN_AMOUNT:
            discounted_amount = cls.MIN_AMOUNT
        return cls(discounted_amount)
