"""
E-COMMERCE MANAGEMENT SYSTEM (VERSION 2)
----------------------------------------
Features:
1. Login System (Admin, Customer, Cashier)
2. Role-Based Access Control
3. Product Purchasing
4. Coupon Validation
5. Location-Based Tax Calculation
6. Tiered Discounts
7. Receipt Generation
8. Menu Loops
9. Functions and Nested Conditions

Author: Student Assignment Submission
"""

users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "customer": {"password": "cust123", "role": "Customer"},
    "cashier": {"password": "cash123", "role": "Cashier"}
}

sales_history = []


def login():
    print("\n===== LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")

    if username in users:
        if users[username]["password"] == password:
            print(f"\nLogin Successful! Welcome {users[username]['role']}")
            return username, users[username]["role"]
        else:
            print("Incorrect Password.")
    else:
        print("User Not Found.")

    return None, None


def calculate_order():
    print("\n===== PRODUCT PURCHASE =====")

    product = input("Product Name: ")
    quantity = int(input("Quantity: "))
    unit_price = float(input("Unit Price: "))

    subtotal = quantity * unit_price

    print(f"\nSubtotal = {subtotal:.2f}")

    coupon = input(
        "Coupon Code (SAVE10, SAVE20, SAVE30 or NONE): "
    ).upper()

    discount = 0

    if subtotal >= 1000:
        discount += subtotal * 0.15
    else:
        if subtotal >= 500:
            discount += subtotal * 0.10
        else:
            discount += subtotal * 0.05

    if coupon == "SAVE30":
        discount += subtotal * 0.30
    elif coupon == "SAVE20":
        discount += subtotal * 0.20
    elif coupon == "SAVE10":
        discount += subtotal * 0.10
    elif coupon == "NONE":
        pass
    else:
        print("Invalid Coupon Code!")

    location = input(
        "Location (UGANDA, KENYA, TANZANIA): "
    ).upper()

    if location == "UGANDA":
        tax_rate = 0.18
    elif location == "KENYA":
        tax_rate = 0.16
    elif location == "TANZANIA":
        tax_rate = 0.15
    else:
        tax_rate = 0.10
        print("Unknown location. Default tax applied.")

    discounted_amount = subtotal - discount
    tax = discounted_amount * tax_rate
    final_price = discounted_amount + tax

    receipt = {
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "final_price": final_price
    }

    sales_history.append(receipt)

    print("\n========== RECEIPT ==========")
    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: {unit_price:.2f}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"TOTAL PAYABLE: {final_price:.2f}")
    print("=============================")


def view_sales():
    print("\n===== SALES HISTORY =====")

    if not sales_history:
        print("No sales recorded.")
        return

    for i, sale in enumerate(sales_history, start=1):
        print(f"\nSale #{i}")
        print(f"Product: {sale['product']}")
        print(f"Total Paid: {sale['final_price']:.2f}")


def admin_menu():
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Process Order")
        print("2. View Sales History")
        print("3. View Users")
        print("4. Logout")

        choice = input("Choose Option: ")

        if choice == "1":
            calculate_order()

        elif choice == "2":
            view_sales()

        elif choice == "3":
            print("\nRegistered Users")
            for user in users:
                print(f"{user} - {users[user]['role']}")

        elif choice == "4":
            print("Logging Out...")
            break

        else:
            print("Invalid Option.")


def customer_menu():
    while True:
        print("\n===== CUSTOMER MENU =====")
        print("1. Shop / Checkout")
        print("2. Logout")

        choice = input("Choose Option: ")

        if choice == "1":
            calculate_order()

        elif choice == "2":
            print("Logging Out...")
            break

        else:
            print("Invalid Option.")


def cashier_menu():
    while True:
        print("\n===== CASHIER MENU =====")
        print("1. Process Sale")
        print("2. View Sales")
        print("3. Logout")

        choice = input("Choose Option: ")

        if choice == "1":
            calculate_order()

        elif choice == "2":
            view_sales()

        elif choice == "3":
            print("Logging Out...")
            break

        else:
            print("Invalid Option.")


def main():
    while True:
        print("\n==============================")
        print(" E-COMMERCE MANAGEMENT SYSTEM ")
        print("==============================")

        username, role = login()

        if role == "Admin":
            admin_menu()

        elif role == "Customer":
            customer_menu()

        elif role == "Cashier":
            cashier_menu()

        else:
            print("Login Failed.")

        again = input("\nReturn to Login Screen? (Y/N): ").upper()

        if again != "Y":
            print("\nThank you for using the system.")
            break


if __name__ == "__main__":
    main()
