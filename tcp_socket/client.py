import sys
import socket


if __name__ == '__main__':
    server_addr = sys.argv[1]
    port = 9487
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.connect((server_addr, port))
    print("Server connected")
    while True:
        data = raw_input(">> ")
        sock.sendall(data)

        recv_data = sock.recv(25)
        print("recv data: ", recv_data)
