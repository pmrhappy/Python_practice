import socket


if __name__ == '__main__':
    buffer_size = 25
    max_allow_conn = 30
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("ip: ", ip)
    socket_addr = ip
    port = 9487
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind((socket_addr, port))
    sock.listen(max_allow_conn)
    print("Server start listening...")
    while True:
        conn, client_addr = sock.accept()
        print(client_addr, " is connected!!")
        while True:
            data = conn.recv(buffer_size)
            print("data: ", data)
            conn.sendall("Got the data: " + data)
