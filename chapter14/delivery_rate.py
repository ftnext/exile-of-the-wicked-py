"""14.2 ユニットテストを用いたリファクタリングの例（写経）"""
from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class Product:
    """商品クラス"""

    price: int


class DeliveryManager:
    """配送管理クラス"""

    @staticmethod
    def delivery_charge(products: Sequence[Product]) -> int:
        """配送料を返す"""
        charge = 0
        total_price = 0
        for product in products:
            total_price += product.price
        if total_price < 2000:
            charge = 500
        else:
            charge = 0
        return charge
