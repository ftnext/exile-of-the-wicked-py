from dataclasses import dataclass


@dataclass
class Money:
    """
    >>> Money(100)
    Money(amount=100)
    """

    amount: int
