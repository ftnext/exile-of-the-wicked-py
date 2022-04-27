from typing import Final


class HitPoint:
    """ヒットポイント（HP）を表現するクラス"""

    MIN: Final[int] = 0
    MAX: Final[int] = 999

    def __init__(self, value: int) -> None:
        """
        >>> hp = HitPoint(100)

        >>> hp = HitPoint(0)
        >>> hp = HitPoint(-1)
        Traceback (most recent call last):
          ...
        ValueError: 0以上を指定してください

        >>> hp = HitPoint(999)
        >>> hp = HitPoint(1000)
        Traceback (most recent call last):
          ...
        ValueError: 999以下を指定してください
        """
        if value < self.MIN:
            raise ValueError(f"{self.MIN}以上を指定してください")
        if value > self.MAX:
            raise ValueError(f"{self.MAX}以下を指定してください")

        self.value = value
