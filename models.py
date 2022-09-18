# -*- coding: utf-8 -*-
from typing import TypedDict


def currency_rounding(val: float) -> float:
    return round(round(val * 1000 / 10) / 100, 2)


class Product:
    def __init__(self, name: str, unit_price_excl_tax: float):
        self.name = name
        self.unit_price_excl_tax = currency_rounding(unit_price_excl_tax)


class ShoppingCartEntry(TypedDict):
    product: Product
    quantity: int


class ShoppingCart:
    def __init__(self, sales_tax_rate: float = 0.0):
        self.products: ShoppingCartEntry = {}
        self.sales_tax_rate = sales_tax_rate

    @property
    def num_items(self) -> int:
        return sum(self.products.values()) if self.products else 0

    @property
    def total(self) -> float:
        return currency_rounding(self.total_pre_tax + self.total_sales_tax)

    @property
    def total_pre_tax(self) -> float:
        pre_tax_total = 0

        for product, qty in self.products.items():
            pre_tax_total += product.unit_price_excl_tax * qty

        return currency_rounding(pre_tax_total)

    @property
    def total_sales_tax(self) -> float:
        return currency_rounding(self.total_pre_tax * self.sales_tax_rate)

    def add_item(self, product: Product, quantity: int) -> None:
        if product in self.products.keys():
            self.products[product] += quantity
        else:
            self.products[product] = quantity
