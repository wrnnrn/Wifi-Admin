import socket
import sys

print("Client-server archive Dev")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
sock.bind(server_address)
print(f'Starting at {server_address}')
sock.listen(1)

while True:
    print("Waiting connection")
    # The server accept the client
    connection, client_address = sock.accept()
    
    try:
        print('Connection from', client_address)
    
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print("Returning data to the client")
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        connection.close()
