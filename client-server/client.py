import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)
print("Connecting to {server_address}")
sock.connect(server_address)

try:
    with open("message_send.txt", "r") as file:
        message = file.read()
        print(f"Sending {message!r}")
        sock.sendall(message.encode())

        amount_recived = 0
        amount_expected = len(message)

        while amount_recived < amount_expected:
            data = sock.recv(16)
            amount_recived += len(data)
            print(f"Recived {data!r}")

finally:
    print("Closing connection with the server")
    sock.close()
