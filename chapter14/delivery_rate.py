"""14.2 ユニットテストを用いたリファクタリングの例（写経）"""
from collections.abc import Sequence
from dataclasses import dataclass
from unittest import TestCase


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


class DeliveryCharge:
    def __init__(self, shopping_cart: ShoppingCart) -> None:
        self.amount = -1


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


class DeliveryChargeTest(TestCase):
    def test_pay_charge(self):
        """商品の合計金額が2000円未満の場合、配送料は500円。"""
        empty_cart = ShoppingCart()
        one_product_added = empty_cart.add(Product(1, "商品A", 500))
        two_product_added = one_product_added.add(Product(2, "商品B", 1499))
        charge = DeliveryCharge(two_product_added)

        self.assertEqual(500, charge.amount)

    def test_free_charge(self):
        """商品の合計金額が2000円以上の場合、配送料は無料。"""
        empty_cart = ShoppingCart()
        one_product_added = empty_cart.add(Product(1, "商品A", 500))
        two_product_added = one_product_added.add(Product(2, "商品B", 1500))
        charge = DeliveryCharge(two_product_added)

        self.assertEqual(0, charge.amount)


if __name__ == "__main__":
    import unittest

    unittest.main()
