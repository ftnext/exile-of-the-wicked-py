from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class RegularPrice:
    MIN_AMOUNT: ClassVar[int] = 0
    amount: int

    def __post_init__(self):
        if self.amount < self.MIN_AMOUNT:
            raise ValueError("価格が0以上でありません")


@dataclass(frozen=True)
class RegularDiscountedPrice:
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
    MIN_AMOUNT: ClassVar[int] = 0
    DISCOUNT_AMOUNT: ClassVar[int] = 300
    amount: int

    @classmethod
    def from_price(cls, price: RegularPrice):
        discounted_amount = price.amount - cls.DISCOUNT_AMOUNT
        if discounted_amount < cls.MIN_AMOUNT:
            discounted_amount = cls.MIN_AMOUNT
        return cls(discounted_amount)
