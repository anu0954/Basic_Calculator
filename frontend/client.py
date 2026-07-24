import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

while True:

    print("\n" + "=" * 35)
    print("     BASIC CALCULATOR")
    print("=" * 35)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "5":
        print("Thank you for using the calculator.")
        break

    try:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        print("Result =", proxy.add(num1, num2))

    elif choice == "2":
        print("Result =", proxy.sub(num1, num2))

    elif choice == "3":
        print("Result =", proxy.mul(num1, num2))

    elif choice == "4":
        print("Result =", proxy.div(num1, num2))

    else:
        print("Invalid Choice")