from abc import ABC, abstractmethod


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
