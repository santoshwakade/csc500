# Step 1: Define the ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_description="", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")


# Step 2: Define the ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                found = True
                # Modify the item details if non-default values are provided
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


# Step 3: Define the print_menu function
def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: """

    option = ""
    while option != "q":
        option = input(menu).lower()

        if option == "a":
            # Add item to cart
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(item)
            print(f"{item_name} added to the cart.")

        elif option == "r":
            # Remove item from cart
            item_name = input("Enter the name of the item to remove: ")
            cart.remove_item(item_name)

        elif option == "c":
            # Modify item quantity
            item_name = input("Enter the item name to modify: ")
            item_description = input("Enter the item description: ")
            new_price = float(input("Enter the new price (or 0 to skip): "))
            new_quantity = int(input("Enter the new quantity (or 0 to skip): "))
            modified_item = ItemToPurchase(item_name, item_description, new_price, new_quantity)
            cart.modify_item(modified_item)

        elif option == "i":
            # Output items' descriptions
            cart.print_descriptions()

        elif option == "o":
            # Output shopping cart
            cart.print_total()

        elif option == "q":
            print("Exiting the program.")

        else:
            print("Invalid option, please choose a valid menu option.")


# Step 4: Main function
def main():
    # Create a shopping cart object
    customer_name = input("Enter the customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)

    # Call the menu
    print_menu(cart)


# Run the main function
if __name__ == "__main__":
    main()
