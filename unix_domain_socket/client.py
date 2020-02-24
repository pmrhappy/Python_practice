import socket


if __name__ == '__main__':
    buffer_size = 25
    server_socket_path = '/tmp/test_uds_server'
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
    sock.connect(server_socket_path)
    print("Server connected")
    while True:
        data = raw_input(">> ")
        sock.sendall(data)

        recv_data = sock.recv(buffer_size)
        print("recv data: ", recv_data)
