from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Member:
    level: int
    agility: int
    magic_attack: int
    vitality: int


class Magic(ABC):
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def cost_magic_point(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def attack_power(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def cost_technical_point(self) -> int:
        raise NotImplementedError


class Fire(Magic):
    """
    >>> level, agility, magic_attack, vitality = 10, 20, 13, 7
    >>> member = Member(level, agility, magic_attack, vitality)
    >>> fire = Fire(member)
    """

    def __init__(self, member: Member) -> None:
        self.member = member

    def name(self) -> str:
        raise NotImplementedError

    def cost_magic_point(self) -> int:
        raise NotImplementedError

    def attack_power(self) -> int:
        raise NotImplementedError

    def cost_technical_point(self) -> int:
        raise NotImplementedError
