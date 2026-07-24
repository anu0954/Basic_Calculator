import xmlrpc.client

# connect to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("\nChoose Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    result = proxy.add(num1, num2)
    print("Addition =", result)

elif choice == 2:
    result = proxy.sub(num1, num2)
    print("Subtraction =", result)

elif choice == 3:
    result = proxy.mul(num1, num2)
    print("Multiplication =", result)

elif choice == 4:
    result = proxy.div(num1, num2)
    print("Division =", result)

elif choice == 5:
    print("Exiting program...")

else:
    print("Invalid choice")