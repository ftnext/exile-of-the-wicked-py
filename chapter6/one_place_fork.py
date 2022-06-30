from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Member:
    level: int
    agility: int


class MagicType(Enum):
    FIRE = auto()
    SHIDEN = auto()
    HELL_FIRE = auto()


class Magic:
    """
    >>> level, agility = 10, 20
    >>> member = Member(level, agility)
    >>> Magic(MagicType.FIRE, member)
    Magic(name='ファイア', cost_magic_point=2, attack_power=25, cost_technical_point=0)
    >>> Magic(MagicType.SHIDEN, member)
    Magic(name='紫電', cost_magic_point=7, attack_power=80, cost_technical_point=5)
    """

    def __init__(self, magic_type: MagicType, member: Member) -> None:
        match magic_type:
            case MagicType.FIRE:
                self.name = "ファイア"
                self.cost_magic_point = 2
                self.attack_power = 20 + int(member.level * 0.5)
                self.cost_technical_point = 0
            case MagicType.SHIDEN:
                self.name = "紫電"
                self.cost_magic_point = 5 + int(member.level * 0.2)
                self.attack_power = 50 + int(member.agility * 1.5)
                self.cost_technical_point = 5

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r}, "
            f"cost_magic_point={self.cost_magic_point}, "
            f"attack_power={self.attack_power}, "
            f"cost_technical_point={self.cost_technical_point})"
        )
