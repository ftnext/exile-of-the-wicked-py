from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Member:
    level: int


class MagicType(Enum):
    FIRE = auto()
    SHIDEN = auto()
    HELL_FIRE = auto()


class Magic:
    """
    >>> member = Member(10)
    >>> Magic(MagicType.FIRE, member)
    Magic(name='ファイア', cost_magic_point=2, attack_power=25, cost_technical_point=0)
    """

    def __init__(self, magic_type: MagicType, member: Member) -> None:
        match magic_type:
            case MagicType.FIRE:
                self.name = "ファイア"
                self.cost_magic_point = 2
                self.attack_power = 20 + int(member.level * 0.5)
                self.cost_technical_point = 0

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r}, "
            f"cost_magic_point={self.cost_magic_point}, "
            f"attack_power={self.attack_power}, "
            f"cost_technical_point={self.cost_technical_point})"
        )
