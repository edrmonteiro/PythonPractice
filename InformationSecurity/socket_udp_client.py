import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("client socket created")

host = 'localhost'
port = 5433
message = "Hello from client!! "

try:
    print('client:' + message)
    s.sendto(message.encode(), (host, 5432))
    data, server = s.recvfrom(4096)
    data = data.decode()
    print('Client:' + data)
finally:
    print('client: closing connect')
    s.close()

stop = 1