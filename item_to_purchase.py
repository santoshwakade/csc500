# Define the ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")


# Main function
def main():
    items = []

    # Display the menu
    while True:
        print("\nMenu:")
        print("1. Add an item")
        print("2. Print all items")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Add an item to the shopping cart
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))

            # Create item object and add it to the list
            item = ItemToPurchase(item_name, item_price, item_quantity)
            items.append(item)
            print(f"{item_name} added to cart.")

        elif choice == "2":
            # Print all items in the cart
            if not items:
                print("Your shopping cart is empty.")
            else:
                print("\nItems in the cart:")
                total_cost = 0
                for item in items:
                    item.print_item_cost()
                    total_cost += item.item_price * item.item_quantity
                print(f"\nTotal cost: ${total_cost}")

        elif choice == "3":
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 3.")


# Run the main function
if __name__ == "__main__":
    main()
