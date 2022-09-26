# -*- coding: utf-8 -*-
import unittest

from models import Offer, Product, ShoppingCart


class TestStepFour(unittest.TestCase):
    def test_main_scenario(self):
        # Given:
        # An empty shopping cart
        shopping_cart = ShoppingCart()
        self.assertEqual(shopping_cart.num_items, 0, "Shopping cart is not empty")
        # And a product, Dove Soap with a unit price of 39.99
        product_dove_soap = Product(name="Dove Soap", unit_price_excl_tax=39.99)
        self.assertEqual(
            product_dove_soap.name, "Dove Soap", "Product name is incorrect"
        )
        self.assertEqual(
            product_dove_soap.unit_price_excl_tax, 39.99, "Product price is incorrect"
        )
        # And another product, Axe Deo with a unit price of 99.99
        product_axe_deo = Product(name="Axe Deo", unit_price_excl_tax=99.99)
        self.assertEqual(product_axe_deo.name, "Axe Deo", "Product name is incorrect")
        self.assertEqual(
            product_axe_deo.unit_price_excl_tax, 99.99, "Product price is incorrect"
        )
        # And a sales tax rate of 12.5%
        shopping_cart.sales_tax_rate = 0.125
        # and an offer for dove soap with buy two get one free
        dove_btgof = Offer(product=product_dove_soap, qualifying_qty=2, bonus_qty=1)
        shopping_cart.add_offer(dove_btgof)

        # TODO: add buy one get one free offer

        # When:
        # The user adds 3 Dove Soaps to the shopping cart
        shopping_cart.add_item(product=product_dove_soap, quantity=3)

        # Then:
        self.assertEqual(
            shopping_cart.num_items, 3, "Incorrect number of items in cart"
        )
        self.assertEqual(
            len(shopping_cart.products.keys()), 1, "Incorrect number of cart products"
        )
        self.assertDictEqual(
            shopping_cart.products,
            {product_dove_soap: 3},
            "Cart is incorrect",
        )
        self.assertListEqual(
            shopping_cart.offers,
            [dove_btgof],
            "Cart has incorrect offers",
        )
        # The shopping cart should contain 3 Dove Soaps each with a unit price of 39.99
        self.assertEqual(
            shopping_cart.products[product_dove_soap],
            3,
            "Cart has incorrect number of Dove Soap items",
        )
        self.assertEqual(
            list(shopping_cart.products.keys())[0].name,
            "Dove Soap",
            "Cart item name incorrect",
        )
        self.assertEqual(
            list(shopping_cart.products.keys())[0].unit_price_excl_tax,
            39.99,
            "Cart unit price incorrect",
        )
        # And the shopping cart should contain no Axe Deos
        self.assertTrue(
            product_axe_deo not in shopping_cart.products.keys(),
            "Cart has axe deodorant items",
        )

        # And the total sales tax amount for the shopping cart should equal 10.00
        self.assertEqual(shopping_cart.total_sales_tax, 10.00, "Incorrect sales tax")
        # And the shopping cart’s total price should equal 89.98
        self.assertEqual(shopping_cart.total, 89.98, "Incorrect cart total")

        # TODO: check discount amount


if __name__ == "__main__":
    unittest.main()
