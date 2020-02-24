import socket
import os


if __name__ == '__main__':
    buffer_size = 25
    socket_path = '/tmp/test_uds_server'
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
    os.unlink(socket_path)
    sock.bind(socket_path)
    sock.listen(1)
    print("Server start listening...")
    while True:
        conn, client_addr = sock.accept()
        print(client_addr, " is connected!!")
        while True:
            data = conn.recv(buffer_size)
            print("data: ", data)
            conn.sendall("Got the data: " + data)
