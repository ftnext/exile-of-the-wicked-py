from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    """
    >>> Money(100)
    Money(amount=100)

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

    amount: int
