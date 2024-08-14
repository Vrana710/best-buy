# store.py

from typing import List, Sequence
from products import Product

class Store:
    """
    A class to represent the store containing products.

    Attributes:
        products (List[Product]): A list of products in the store.
    """

    def __init__(self, products: List[Product]):
        """
        Constructs all the necessary attributes for the store object.

        Args:
            products (List[Product]): A list of Product objects to initialize the store.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a product to the store.

        Args:
            product (Product): The product to add to the store.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove from the store.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Gets the total quantity of all active products in the store.

        Returns:
            int: The total quantity of all active products.
        """
        return sum(product.get_quantity() for product in self.products if product.is_active())

    def get_all_products(self) -> List[Product]:
        """
        Gets all active products in the store.

        Returns:
            List[Product]: A list of all active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: Sequence[tuple[Product, int]]) -> float:
        """
        Processes an order, buying the specified quantities of products.

        Args:
            shopping_list (Sequence[tuple[Product, int]]): A list of tuples containing
            products and their respective quantities to purchase.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If any product quantity in the shopping list is invalid.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
