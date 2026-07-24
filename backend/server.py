from xmlrpc.server import SimpleXMLRPCServer
from calculator import add, sub, mul, div

HOST = "localhost"
PORT = 8000

server = SimpleXMLRPCServer((HOST, PORT))

print("=" * 40)
print(" XML-RPC Calculator Server Started ")
print("=" * 40)
print(f"Running on {HOST}:{PORT}")
print("Waiting for client requests...\n")

server.register_function(add)
server.register_function(sub)
server.register_function(mul)
server.register_function(div)

server.serve_forever()