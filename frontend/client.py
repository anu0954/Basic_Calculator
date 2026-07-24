import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

while True:
    print("\n" + "=" * 40)
    print("        BASIC CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    # Validate number input
    try:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    if choice == "1":
        result = proxy.add(num1, num2)
        print(f"\nResult = {result}")

    elif choice == "2":
        result = proxy.sub(num1, num2)
        print(f"\nResult = {result}")

    elif choice == "3":
        result = proxy.mul(num1, num2)
        print(f"\nResult = {result}")

    elif choice == "4":
        result = proxy.div(num1, num2)
        print(f"\nResult = {result}")

    else:
        print("Invalid choice! Please select between 1 and 5.")