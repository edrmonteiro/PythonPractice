import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket server created!!')

host = 'localhost'
port = 5432

s.bind((host, port))
message = 'Hello from server!!'

while 1:
    data, end = s.recvfrom(4096)

    if data:
        print('Server sending message')
        s.sendto(data + (message.encode()), end)

stop = 1