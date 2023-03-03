"""14.2 ユニットテストを用いたリファクタリングの例（写経）"""
from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    """商品クラス"""

    id: int
    name: str
    price: int


class ShoppingCart:
    def __init__(self, products: list[Product] | None = None) -> None:
        self.products: list[Product] = products or []

    def add(self, product: Product) -> "ShoppingCart":
        adding = list(self.products)
        adding.append(product)
        return self.__class__(adding)


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
