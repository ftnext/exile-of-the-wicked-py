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
    >>> fire.name()
    'ファイア'
    >>> fire.cost_magic_point()
    2
    >>> fire.attack_power()
    25
    >>> fire.cost_technical_point()
    0
    """

    def __init__(self, member: Member) -> None:
        self.member = member

    def name(self) -> str:
        return "ファイア"

    def cost_magic_point(self) -> int:
        return 2

    def attack_power(self) -> int:
        return 20 + int(self.member.level * 0.5)

    def cost_technical_point(self) -> int:
        return 0


class Shiden(Magic):
    """
    >>> level, agility, magic_attack, vitality = 10, 20, 13, 7
    >>> member = Member(level, agility, magic_attack, vitality)
    >>> shiden = Shiden(member)
    >>> shiden.name()
    '紫電'
    >>> shiden.cost_magic_point()
    7
    >>> shiden.attack_power()
    80
    >>> shiden.cost_technical_point()
    5
    """

    def __init__(self, member: Member) -> None:
        self.member = member

    def name(self) -> str:
        return "紫電"

    def cost_magic_point(self) -> int:
        return 5 + int(self.member.level * 0.2)

    def attack_power(self) -> int:
        return 50 + int(self.member.agility * 1.5)

    def cost_technical_point(self) -> int:
        return 5
