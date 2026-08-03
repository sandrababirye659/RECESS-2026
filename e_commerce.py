
ROLE_CREDENTIALS = {
	"admin": "admin123",
	"customer": "customer123",
	"cashier": "cashier123",
}

COUPON_DISCOUNTS = {
	"SAVE10": 0.10,
	"SAVE20": 0.20,
	"VIP25": 0.25,
}

TAX_RATES = {
	"local": 0.05,
	"state": 0.08,
	"international": 0.15,
}


def get_discount_rate(subtotal):
	if subtotal < 0:
		return None
	if subtotal < 100:
		return 0.05
	elif subtotal < 500:
		return 0.10
	else:
		return 0.15


def get_coupon_discount(coupon_code):
	coupon_code = coupon_code.strip().upper()
	if coupon_code == "":
		return 0.0, "No coupon used."

	if coupon_code in COUPON_DISCOUNTS:
		return COUPON_DISCOUNTS[coupon_code], f"Coupon {coupon_code} applied."
	return None, "Invalid coupon code."


def get_tax_rate(location):
	location = location.strip().lower()
	if location in TAX_RATES:
		return TAX_RATES[location], f"Tax rate for {location} selected."
	return None, "Invalid tax location."


def calculate_final_price(subtotal, coupon_code, location):
	subtotal_discount = get_discount_rate(subtotal)
	if subtotal_discount is None:
		return None, "Subtotal must be a positive number."

	coupon_discount, coupon_message = get_coupon_discount(coupon_code)
	if coupon_discount is None:
		return None, coupon_message

	tax_rate, tax_message = get_tax_rate(location)
	if tax_rate is None:
		return None, tax_message

	total_discount_rate = subtotal_discount + coupon_discount
	if total_discount_rate > 0.50:
		total_discount_rate = 0.50

	discount_amount = subtotal * total_discount_rate
	discounted_subtotal = subtotal - discount_amount
	tax_amount = discounted_subtotal * tax_rate
	final_price = discounted_subtotal + tax_amount

	return {
		"subtotal": subtotal,
		"subtotal_discount_rate": subtotal_discount,
		"coupon_discount_rate": coupon_discount,
		"discount_amount": discount_amount,
		"tax_rate": tax_rate,
		"tax_amount": tax_amount,
		"final_price": final_price,
	}, f"{coupon_message} {tax_message}"


def prompt_float(message):
	while True:
		value = input(message).strip()
		try:
			return float(value)
		except ValueError:
			print("Please enter a valid number.")


def run_price_calculator():
	print("\n--- Price Calculator ---")
	subtotal = prompt_float("Enter subtotal: ")
	coupon_code = input("Enter coupon code (or press Enter for none): ")
	location = input("Enter tax location (local/state/international): ")

	result, message = calculate_final_price(subtotal, coupon_code, location)
	if result is None:
		print(message)
		return

	print("\nCalculation summary")
	print(f"Subtotal: {result['subtotal']:.2f}")
	print(f"Subtotal discount: {result['subtotal_discount_rate'] * 100:.0f}%")
	print(f"Coupon discount: {result['coupon_discount_rate'] * 100:.0f}%")
	print(f"Discount amount: {result['discount_amount']:.2f}")
	print(f"Tax rate: {result['tax_rate'] * 100:.0f}%")
	print(f"Tax amount: {result['tax_amount']:.2f}")
	print(f"Final price: {result['final_price']:.2f}")
	print(message)


def show_pricing_rules():
	print("\n--- Pricing Rules ---")
	print("Subtotal discounts:")
	print("  Below 100: 5%")
	print("  100 to 499.99: 10%")
	print("  500 and above: 15%")
	print("Coupons:")
	for code, rate in COUPON_DISCOUNTS.items():
		print(f"  {code}: {rate * 100:.0f}%")
	print("Tax locations:")
	for location, rate in TAX_RATES.items():
		print(f"  {location}: {rate * 100:.0f}%")


def login():
	print("--- E-Commerce Login ---")
	username = input("Username: ").strip().lower()
	password = input("Password: ").strip()

	if username in ROLE_CREDENTIALS and ROLE_CREDENTIALS[username] == password:
		return username
	return None


def admin_menu():
	while True:
		print("\n--- Admin Menu ---")
		print("1. View pricing rules")
		print("2. Calculate price")
		print("3. Logout")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			show_pricing_rules()
		elif choice == "2":
			run_price_calculator()
		elif choice == "3":
			break
		else:
			print("Invalid choice.")


def customer_menu():
	while True:
		print("\n--- Customer Menu ---")
		print("1. Calculate price")
		print("2. Logout")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			run_price_calculator()
		elif choice == "2":
			break
		else:
			print("Invalid choice.")


def cashier_menu():
	while True:
		print("\n--- Cashier Menu ---")
		print("1. Calculate price")
		print("2. View checkout note")
		print("3. Logout")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			run_price_calculator()
		elif choice == "2":
			print("Checkout note: verify subtotal, coupon, and tax location before payment.")
		elif choice == "3":
			break
		else:
			print("Invalid choice.")


def main():
	print("Simple E-Commerce Application")

	while True:
		role = login()
		if role == "admin":
			print("Login successful. Welcome, Admin.")
			admin_menu()
		elif role == "customer":
			print("Login successful. Welcome, Customer.")
			customer_menu()
		elif role == "cashier":
			print("Login successful. Welcome, Cashier.")
			cashier_menu()
		else:
			print("Invalid username or password.")

		again = input("\nWould you like to log in again? (y/n): ").strip().lower()
		if again != "y":
			print("Goodbye.")
			break


if __name__ == "__main__":
	main()
