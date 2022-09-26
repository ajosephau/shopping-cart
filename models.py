# -*- coding: utf-8 -*-
"""Shopping cart models

This module has all shopping cart models and a support function for generating currency rounding.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html

"""
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


class Offer:
    """An abstraction of a offer for a product in our shopping cart

    Attributes:
        product (Product): product with offer.
        qualifying_qty (int): number of Product's to buy to qualify for offer
        bonus_qty (int): number of Product's with no cost once qualitfy for offer
    """

    def __init__(self, product: Product, qualifying_qty: int, bonus_qty: int):
        self.product = product
        self.qualifying_qty = qualifying_qty
        self.bonus_qty = bonus_qty


class ShoppingCart:
    """An abstraction of our shopping cart.

    Attributes:
        sales_tax_rate (float): Sales tax to be applied on shopping cart

    """

    def __init__(self, sales_tax_rate: float = 0.0):
        self.products: Dict[Product, int] = {}
        self.sales_tax_rate = sales_tax_rate
        self.offers = []

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
            post_offer_qty = qty
            # process any applicable offers
            for offer in self.offers:
                if offer.product == product:
                    num_times_qualify_for_offer = int(
                        post_offer_qty / (offer.qualifying_qty + offer.bonus_qty)
                    )
                    post_offer_qty = num_times_qualify_for_offer * offer.qualifying_qty
            pre_tax_total += product.unit_price_excl_tax * post_offer_qty

        return currency_rounding(pre_tax_total)

    @property
    def total_sales_tax(self) -> float:
        """float: the tax component of this shopping cart."""
        return currency_rounding(self.total_pre_tax * self.sales_tax_rate)

    def add_offer(self, offer: Offer) -> None:
        """Adds an offer to the shopping cart.

        Args:
            offer: The offer to be added.

        Returns:
            None

        """
        self.offers.append(offer)

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
