import socket
import sys
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("The connection fail!!!")
        print("error: {}".format(e))
        sys.exit()

    print("Socket successful created")

    host_target = input("type IP:")
    port_target = input("type the port:")

    try:
        s.connect((host_target, int(port_target)))
        print('connected')
        s.shutdown(2)
    except socket.error as e:
        print("Connection fail {}", e)

if __name__ == '__main__':
    main()

stop = 1