from typing import List, Sequence
from products import Product

class Store:
    """A class to represent the store containing products."""

    def __init__(self, products: List[Product]):
        """Constructs all the necessary attributes for the store object."""
        self.products = products

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Gets the total quantity of all products in the store."""
        return sum(product.get_quantity() 
                   for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Gets all active products in the store."""
        return [product for product in self.products 
                            if product.is_active()]

    def order(self, shopping_list: 
                Sequence[tuple[Product, int]]) -> float:
        """Processes an order, buying the specified 
        quantities of products."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
