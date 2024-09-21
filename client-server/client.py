import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)
print("Connecting to {server_address}")
sock.connect(server_address)


