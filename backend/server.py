from xmlrpc.server import SimpleXMLRPCServer
from calculator import add, sub, mul, div


HOST = "localhost"
PORT = 8000


server = SimpleXMLRPCServer(
    (HOST, PORT),
    allow_none=True
)


print("================================")
print(" XML RPC Calculator Server ")
print("================================")
print(f"Running at {HOST}:{PORT}")


server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(mul, "mul")
server.register_function(div, "div")


try:
    server.serve_forever()

except KeyboardInterrupt:
    print("\nServer stopped")