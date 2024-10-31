class Product:
    """Represents a product in the store."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Inventory:
    """Manages the store's products."""

    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity=1):
        """Add a product to the inventory."""
        if product.name in self.products:
            self.products[product.name]['quantity'] += quantity
        else:
            self.products[product.name] = {'product': product, 'quantity': quantity}

    def list_products(self):
        """List all products available in the store."""
        product_list = []
        for item in self.products.values():
            product, quantity = item['product'], item['quantity']
            product_list.append(f"{product} (In stock: {quantity})")
        return "\n".join(product_list)


class Cart:
    """Manages the user's cart."""

    def __init__(self):
        self.items = {}

    def add_to_cart(self, product):
        """Add a product to the cart."""
        if product.name in self.items:
            self.items[product.name]['quantity'] += 1
        else:
            self.items[product.name] = {'product': product, 'quantity': 1}

    def remove_from_cart(self, product_name):
        """Remove a product from the cart."""
        if product_name in self.items:
            if self.items[product_name]['quantity'] > 1:
                self.items[product_name]['quantity'] -= 1
            else:
                del self.items[product_name]

    def view_cart(self):
        """Display the contents of the cart."""
        if not self.items:
            return "Your cart is empty."
        cart_list = []
        for item in self.items.values():
            product, quantity = item['product'], item['quantity']
            cart_list.append(f"{product} (Quantity: {quantity})")
        return "\n".join(cart_list)

    def checkout(self):
        """Calculate total price and clear the cart."""
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        self.items.clear()
        return f"Total: ${total:.2f}. Thank you for shopping with us!"


class ChatBot:
    """Main interface for interacting with the user."""

    def __init__(self):
        self.inventory = Inventory()
        self.cart = Cart()

    def handle_command(self, command):
        """Handle a command from the user."""
        command = command.lower()

        if command == "list products":
            return self.inventory.list_products()

        elif command.startswith("add to cart"):
            product_name = command[len("add to cart "):].strip()
            if product_name in self.inventory.products:
                product = self.inventory.products[product_name]['product']
                self.cart.add_to_cart(product)
                return f"Added {product_name} to cart."
            else:
                return "Product not found."

        elif command.startswith("remove from cart"):
            product_name = command[len("remove from cart "):].strip()
            if product_name in self.cart.items:
                self.cart.remove_from_cart(product_name)
                return f"Removed {product_name} from cart."
            else:
                return "Product not in cart."

        elif command == "view cart":
            return self.cart.view_cart()

        elif command == "checkout":
            return self.cart.checkout()

        else:
            return "Sorry, I didn't understand that command."


# Example usage
if __name__ == "__main__":
    # Initialize chatbot and inventory
    bot = ChatBot()

    # Add some products to inventory
    bot.inventory.add_product(Product("Laptop", 999.99), quantity=5)
    bot.inventory.add_product(Product("Smartphone", 499.99), quantity=10)
    bot.inventory.add_product(Product("Headphones", 199.99), quantity=15)

    # Simulate user interaction
    print(bot.handle_command("list products"))
    print(bot.handle_command("add to cart Laptop"))
    print(bot.handle_command("view cart"))
    print(bot.handle_command("add to cart Smartphone"))
    print(bot.handle_command("view cart"))
    print(bot.handle_command("checkout"))
