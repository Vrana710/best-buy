from products import Product
from store import Store


def start(store: Store):
    """
    Starts the user interface for the store.

    Args:
        store (Store): The store object.
    """
    while True:
        print("\n1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            products = store.get_all_products()
            for product in products:
                print(product.show())
        elif choice == '2':
            print(f"Total amount in store: {store.get_total_quantity()}")
        elif choice == '3':
            products = store.get_all_products()
            shopping_list = []
            for product in products:
                quantity = int(input(f"Enter quantity for {product.name}: "))
                shopping_list.append((product, quantity))
            total_price = store.order(shopping_list)
            print(f"Total price: {total_price}")
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")


def main():
    """
    Initializes the store with default products and starts the user interface.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
