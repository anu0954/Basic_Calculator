from xmlrpc.server import SimpleXMLRPCServer

# Function to perform addition
def add(a, b):
    print("Client required addition")
    return a + b

def sub(a, b):
    print("Client required Subtraction")
    return a - b

def mul(a, b):
    print("Client required multiplication")
    return a * b

def div(a, b):
    print("Client required Division")
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Create server
server = SimpleXMLRPCServer(("localhost", 8000))

print("server started...")
print("waiting for the client request...")

# Register functions
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(mul, "mul")
server.register_function(div, "div")

# Keep server running
server.serve_forever()