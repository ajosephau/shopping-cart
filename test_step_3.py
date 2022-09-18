# -*- coding: utf-8 -*-
import unittest

from models import Product, ShoppingCart


class TestStepThree(unittest.TestCase):
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

        # When:
        # The user adds 2 Dove Soaps to the shopping cart
        shopping_cart.add_item(product=product_dove_soap, quantity=2)
        # And then adds 2 Axe Deos to the shopping cart
        shopping_cart.add_item(product=product_axe_deo, quantity=2)

        # Then:
        self.assertEqual(
            shopping_cart.num_items, 4, "Incorrect number of items in cart"
        )
        self.assertEqual(
            len(shopping_cart.products.keys()), 2, "Incorrect number of cart products"
        )
        self.assertDictEqual(
            shopping_cart.products,
            {product_dove_soap: 2, product_axe_deo: 2},
            "Cart is incorrect",
        )
        # The shopping cart should contain 2 Dove Soaps each with a unit price of 39.99
        self.assertEqual(
            shopping_cart.products[product_dove_soap],
            2,
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
        # And the shopping cart should contain 2 Axe Deos each with a unit price of 99.99
        self.assertEqual(
            shopping_cart.products[product_axe_deo],
            2,
            "Cart has incorrect number of Axe Deo items",
        )
        self.assertEqual(
            list(shopping_cart.products.keys())[1].name,
            "Axe Deo",
            "Cart item name incorrect",
        )
        self.assertEqual(
            list(shopping_cart.products.keys())[1].unit_price_excl_tax,
            99.99,
            "Cart unit price incorrect",
        )
        # And the total sales tax amount for the shopping cart should equal 35.00
        self.assertEqual(shopping_cart.total_sales_tax, 35.00, "Incorrect sales tax")
        # And the shopping cart’s total price should equal 314.96
        self.assertEqual(shopping_cart.total, 314.96, "Incorrect cart total")


if __name__ == "__main__":
    unittest.main()
