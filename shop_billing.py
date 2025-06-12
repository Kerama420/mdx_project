products = {
    "Sprite": 80,
    "Coca-cola": 80,
    "Fanta Orange": 80,
    "Pepsi": 95,
    "Seven-up": 95
}

basket = {}

def welcome_user():
    name = input("Welcome! Please enter your name: ")
    print(f"Hello {name}, welcome to my Soda Shop!")
    return name

def show_products():
    print("\nAvailable Items:")
    for item, price in products.items():
        print(f"- {item}: ${price:.2f}")

def add_to_basket():
    show_products()
    item = input("Enter item to add: ").title()
    if item in products:
        try:
            quantity = int(input(f"How many {item}s would you like to add? "))
            if quantity <= 0:
                print("Please enter a positive number.")
                return
            basket[item] = basket.get(item, 0) + quantity
            print(f"{quantity} {item}(s) added to basket.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Item not found. Please choose from the available products.")

def view_basket():
    print("\nYour Basket:")
    if not basket:
        print("Basket is empty.")
    else:
        for item, quantity in basket.items():
            print(f"{item} x {quantity} @ ${products[item]:.2f} each")

def delete_item_from_basket():
    if not basket:
        print("Basket is already empty.")
        return
    item = input("Enter item to remove: ").title()
    if item in basket:
        try:
            quantity = int(input(f"How many {item}s would you like to remove? "))
            if quantity <= 0:
                print("Please enter a positive number.")
                return
            if quantity >= basket[item]:
                del basket[item]
                print(f"All {item}s removed from basket.")
            else:
                basket[item] -= quantity
                print(f"{quantity} {item}(s) removed.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Item not in basket.")

def apply_discount(total):
    try:
        discount = float(input("Enter discount percentage (e.g. 10 for 10%): "))
        if 0 <= discount <= 100:
            discount_amount = total * (discount / 100)
            total -= discount_amount
            print(f"Discount of {discount}% applied. New total: ${total:.2f}")
        else:
            print("Invalid discount range. No discount applied.")
    except ValueError:
        print("Invalid input. No discount applied.")
    return total

def calculate_total():
    total = 0
    for item, quantity in basket.items():
        total += products[item] * quantity
    print(f"\nTotal before discount: ${total:.2f}")
    total = apply_discount(total)
    print(f"Final total: ${total:.2f}")
    print("Thank you for your purchase!")

def main():
    welcome_user()
    while True:
        print("\nMenu:")
        print("1. View Products")
        print("2. Add to Basket")
        print("3. View Basket")
        print("4. Remove from Basket")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()
        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_basket()
        elif choice == "3":
            view_basket()
        elif choice == "4":
            delete_item_from_basket()
        elif choice == "5":
            calculate_total()
        elif choice == "6":
            print("Thank you for shopping with us!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
