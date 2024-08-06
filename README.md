# Best Buy Tech Store

## Overview

This project simulates a tech equipment store like "Best Buy". It allows you to list products, show total quantity, and make orders. The project is implemented in Python and demonstrates basic object-oriented principles, including the use of classes and methods.

## Project Structure

The project contains the following files:

- `main.py`: The entry point of the application which handles the user interface.
- `products.py`: Defines the `Product` class representing individual products.
- `store.py`: Defines the `Store` class representing the store containing multiple products.

## Class Descriptions

### Product Class

Represents a specific type of product available in the store.

**Attributes:**
- `name` (str): The name of the product.
- `price` (float): The price of the product.
- `quantity` (int): The quantity of the product available.
- `active` (bool): The status of the product's availability.

**Methods:**
- `__init__(self, name: str, price: float, quantity: int)`: Initializes a new product.
- `get_quantity(self) -> int`: Returns the quantity of the product.
- `set_quantity(self, quantity: int)`: Sets the quantity of the product and deactivates it if the quantity is 0.
- `is_active(self) -> bool`: Checks if the product is active.
- `activate(self)`: Activates the product.
- `deactivate(self)`: Deactivates the product.
- `show(self) -> str`: Returns a string representation of the product.
- `buy(self, quantity: int) -> float`: Buys a given quantity of the product and returns the total price.

### Store Class

Represents the store containing products.

**Attributes:**
- `products` (List[Product]): A list of products in the store.

**Methods:**
- `__init__(self, products: List[Product])`: Initializes the store with a list of products.
- `add_product(self, product: Product)`: Adds a product to the store.
- `remove_product(self, product: Product)`: Removes a product from the store.
- `get_total_quantity(self) -> int`: Returns the total quantity of all products in the store.
- `get_all_products(self) -> List[Product]`: Returns all active products in the store.
- `order(self, shopping_list: List[tuple]) -> float`: Processes an order and returns the total price.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Vrana710/best-buy.git 
    ```
2. Navigate to the project directory:
    ```sh
    cd best-buy
    ```

### Usage

1. Run the application:
    ```sh
    python3 main.py
    ```
2. Follow the on-screen instructions to interact with the store:
    - List all products in the store.
    - Show the total quantity of items in the store.
    - Make an order by specifying the quantities for each product.
    - Quit the application.

### Example

Here is a quick example of how to use the application:

```sh
$ python3 main.py

1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Choose an option: 1
MacBook Air M2, Price: 1450, Quantity: 100
Bose QuietComfort Earbuds, Price: 250, Quantity: 500
Google Pixel 7, Price: 500, Quantity: 250

Choose an option: 2
Total amount in store: 850

Choose an option: 3
Enter quantity for MacBook Air M2: 1
Enter quantity for Bose QuietComfort Earbuds: 2
Enter quantity for Google Pixel 7: 3
Total price: 3850

Choose an option: 4
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to contact me at [ranavarsha710@gmail.com](mailto:ranavarsha710@gmail.com).
```

### Key Sections Explained:

1. **Overview**: A brief description of the project.
2. **Project Structure**: An outline of the key files in the project.
3. **Class Descriptions**: Detailed descriptions of the `Product` and `Store` classes, including their attributes and methods.
4. **Getting Started**: Instructions on prerequisites, installation, and running the application.
5. **Usage**: An example of how to use the application.
6. **Contributing**: Information on how others can contribute to the project.
7. **License**: Licensing information.
8. **Contact**: How to reach you for questions or suggestions.

