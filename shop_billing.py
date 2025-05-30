# shop_billing.py

items = {
    "Notebook": 2.50,
    "Pen": 1.00,
    "Eraser": 0.50,
    "Pencil": 0.75,
    "Marker": 1.25
}

basket = {}

def greet_user():
    name = input("Welcome! Please enter your name: ")
    print(f"Hello, {name}! Let's start shopping for your stationery.")
    return name

def view_items():
    print("\nAvailable Items:")
    for item, price in items.items():
        print(f"{item} - ${price:.2f}")

def add_to_basket():
    item = input("Enter item name to add: ")
    if item in items:
        quantity = int(input("Enter quantity: "))
        basket[item] = basket.get(item, 0) + quantity
        print(f"Added {quantity} x {item} to your basket.")
    else:
        print("Item not found.")

def view_basket():
    if not basket:
        print("Basket is empty.")
    else:
        print("\nYour Basket:")
        for item, quantity in basket.items():
            print(f"{item} - Quantity: {quantity} - Total: ${items[item] * quantity:.2f}")

def remove_from_basket():
    item = input("Enter item name to remove: ")
    if item in basket:
        del basket[item]
        print(f"{item} removed from basket.")
    else:
        print("Item not found in basket.")

def apply_discount(total):
    try:
        discount = float(input("Enter discount % (0-100): "))
        if 0 <= discount <= 100:
            return total * (1 - discount / 100)
        else:
            print("Invalid discount. Skipping discount.")
            return total
    except ValueError:
        print("Invalid input. No discount applied.")
        return total

def calculate_total():
    total = sum(items[item] * quantity for item, quantity in basket.items())
    total_with_discount = apply_discount(total)
    print(f"\nFinal total after discount: ${total_with_discount:.2f}")

def main():
    greet_user()
    while True:
        print("\nMenu:\n1. View Items\n2. Add Item\n3. View Basket\n4. Remove Item\n5. Checkout\n6. Exit")
        choice = input("Choose option (1-6): ")

        if choice == "1":
            view_items()
        elif choice == "2":
            add_to_basket()
        elif choice == "3":
            view_basket()
        elif choice == "4":
            remove_from_basket()
        elif choice == "5":
            calculate_total()
        elif choice == "6":
            print("Thanks for shopping! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
