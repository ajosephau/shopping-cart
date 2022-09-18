import unittest

from models import ShoppingCart, Product


class TestStepTwo(unittest.TestCase):

    def test_main_scenario(self):
        # Given:
        # An empty shopping cart
        shopping_cart = ShoppingCart()
        self.assertEqual(shopping_cart.num_items, 0, "Shopping cart is not empty")

        # And a product, Dove Soap with a unit price of 39.99
        product_dove_soap = Product(name="Dove Soap", unit_price_excl_tax=39.99)
        self.assertEqual(product_dove_soap.name, "Dove Soap", "Product name is incorrect")
        self.assertEqual(product_dove_soap.unit_price_excl_tax, 39.99, "Product price is incorrect")

        # When:
        # The user adds 5 Dove Soaps to the shopping cart
        shopping_cart.add_item(product=product_dove_soap, quantity=5)

        # And then adds another 3 Dove Soaps to the shopping cart
        shopping_cart.add_item(product=product_dove_soap, quantity=3)

        # Then:
        # The shopping cart should contain 8 Dove Soaps each with a unit price of 39.99
        self.assertEqual(shopping_cart.num_items, 8, "Incorrect number of items in cart")
        self.assertDictEqual(shopping_cart.products, {product_dove_soap: 8}, "Cart is incorrect")
        self.assertEqual(len(shopping_cart.products.keys()), 1, "Multiple items in cart")
        self.assertEqual(list(shopping_cart.products.keys())[0].unit_price_excl_tax, 39.99, "Cart unit price incorrect")

        # And the shopping cart’s total price should equal 199.95
        self.assertEqual(shopping_cart.total, 319.92, "Incorrect cart total")


if __name__ == '__main__':
    unittest.main()
