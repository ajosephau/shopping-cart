# -*- coding: utf-8 -*-
"""Shopping cart models

This module has all shopping cart models and a support function for generating currency rounding.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html

"""

# -*- coding: utf-8 -*-
from typing import Dict


def currency_rounding(val: float) -> float:
    """Rounds a currency value to two decimal places

    Args:
        val (float): The input float value to be rounded

    Returns:
        float: The input currency value rounded to two decimal places
    """
    return round(round(val * 1000 / 10) / 100, 2)


class Product:
    """An abstraction of a product in our shopping cart

    Attributes:
        name (str): Product name.
        unit_price_excl_tax (float): Product's unit price without any taxes

    """

    def __init__(self, name: str, unit_price_excl_tax: float):
        self.name = name
        self.unit_price_excl_tax = currency_rounding(unit_price_excl_tax)


class ShoppingCart:
    """An abstraction of our shopping cart.

    Attributes:
        sales_tax_rate (float): Sales tax to be applied on shopping cart

    """

    def __init__(self, sales_tax_rate: float = 0.0):
        self.products: Dict[Product, int] = {}
        self.sales_tax_rate = sales_tax_rate

    @property
    def num_items(self) -> int:
        """int: Number of items in the shopping cart."""
        return sum(self.products.values()) if self.products else 0

    @property
    def total(self) -> float:
        """float: the total cost of the shopping cart including tax."""
        return currency_rounding(self.total_pre_tax + self.total_sales_tax)

    @property
    def total_pre_tax(self) -> float:
        """float: the total cost of the shopping cart without tax."""
        pre_tax_total = 0

        for product, qty in self.products.items():
            pre_tax_total += product.unit_price_excl_tax * qty

        return currency_rounding(pre_tax_total)

    @property
    def total_sales_tax(self) -> float:
        """float: the tax component of this shopping cart."""
        return currency_rounding(self.total_pre_tax * self.sales_tax_rate)

    def add_item(self, product: Product, quantity: int) -> None:
        """Adds an item to the shopping cart. If one adds the same
        product to the shopping cart the quantity will be updated.

        Args:
            product: The product to be added.
            quantity: The number of product's to be added.

        Returns:
            None

        """
        if product in self.products.keys():
            self.products[product] += quantity
        else:
            self.products[product] = quantity
