from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Member:
    level: int
    agility: int
    magic_attack: int
    vitality: int


@dataclass(frozen=True)
class MagicPoint:
    value: int


@dataclass(frozen=True)
class AttackPower:
    value: int


@dataclass(frozen=True)
class TechnicalPoint:
    value: int


class Magic(ABC):
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def cost_magic_point(self) -> MagicPoint:
        raise NotImplementedError

    @abstractmethod
    def attack_power(self) -> AttackPower:
        raise NotImplementedError

    @abstractmethod
    def cost_technical_point(self) -> TechnicalPoint:
        raise NotImplementedError


class Fire(Magic):
    """
    >>> level, agility, magic_attack, vitality = 10, 20, 13, 7
    >>> member = Member(level, agility, magic_attack, vitality)
    >>> fire = Fire(member)
    >>> fire.name()
    'ファイア'
    >>> fire.cost_magic_point()
    MagicPoint(value=2)
    >>> fire.attack_power()
    AttackPower(value=25)
    >>> fire.cost_technical_point()
    TechnicalPoint(value=0)
    """

    def __init__(self, member: Member) -> None:
        self.member = member

    def name(self) -> str:
        return "ファイア"

    def cost_magic_point(self) -> MagicPoint:
        return MagicPoint(2)

    def attack_power(self) -> AttackPower:
        value = 20 + int(self.member.level * 0.5)
        return AttackPower(value)

    def cost_technical_point(self) -> TechnicalPoint:
        return TechnicalPoint(0)


class Shiden(Magic):
    """
    >>> level, agility, magic_attack, vitality = 10, 20, 13, 7
    >>> member = Member(level, agility, magic_attack, vitality)
    >>> shiden = Shiden(member)
    >>> shiden.name()
    '紫電'
    >>> shiden.cost_magic_point()
    MagicPoint(value=7)
    >>> shiden.attack_power()
    AttackPower(value=80)
    >>> shiden.cost_technical_point()
    TechnicalPoint(value=5)
    """

    def __init__(self, member: Member) -> None:
        self.member = member

    def name(self) -> str:
        return "紫電"

    def cost_magic_point(self) -> MagicPoint:
        value = 5 + int(self.member.level * 0.2)
        return MagicPoint(value)

    def attack_power(self) -> AttackPower:
        value = 50 + int(self.member.agility * 1.5)
        return AttackPower(value)

    def cost_technical_point(self) -> TechnicalPoint:
        return TechnicalPoint(5)


class HellFire(Magic):
    """
    >>> level, agility, magic_attack, vitality = 10, 20, 13, 7
    >>> member = Member(level, agility, magic_attack, vitality)
    >>> hell_fire = HellFire(member)
    >>> hell_fire.name()
    '地獄の業火'
    >>> hell_fire.cost_magic_point()
    MagicPoint(value=16)
    >>> hell_fire.attack_power()
    AttackPower(value=220)
    >>> hell_fire.cost_technical_point()
    TechnicalPoint(value=24)
    """

    def __init__(self, member: Member) -> None:
        self.member = member

    def name(self) -> str:
        return "地獄の業火"

    def cost_magic_point(self) -> MagicPoint:
        return MagicPoint(16)

    def attack_power(self) -> AttackPower:
        value = 200 + int(
            self.member.magic_attack * 0.5 + self.member.vitality * 2
        )
        return AttackPower(value)

    def cost_technical_point(self) -> TechnicalPoint:
        value = 20 + int(self.member.level * 0.4)
        return TechnicalPoint(value)
