from socket import *
import argparse

SERVER_IP = '127.0.0.1'
SERVER_PORT = 10101


def get_file():
    print("Fetching file...")
    client_socket = socket(AF_INET, SOCK_STREAM)

    client_socket.connect((SERVER_IP, SERVER_PORT))
    req = 'GET HelloWorld.html HTTP/1.0\r '
    client_socket.send(req.encode())
    resp = client_socket.recv(2048)
    print('From Server: ', resp.decode())
    client_socket.close()


def get_nested_file():
    print("Fetching nested file...")
    client_socket = socket(AF_INET, SOCK_STREAM)

    client_socket.connect((SERVER_IP, SERVER_PORT))
    req = 'GET htdocs/NestedHelloWorld.html HTTP/1.0\r '
    client_socket.send(req.encode())
    resp = client_socket.recv(2048)
    print('From Server: ', resp.decode())
    client_socket.close()


def get_file_not_found():
    print("Fetching unknown file...")
    client_socket = socket(AF_INET, SOCK_STREAM)

    client_socket.connect((SERVER_IP, SERVER_PORT))
    req = 'GET World.html HTTP/1.0\r '
    client_socket.send(req.encode())
    resp = client_socket.recv(2048)
    print('From Server: ', resp.decode())
    client_socket.close()


def main():
    get_file()
    get_nested_file()
    get_file_not_found()


if __name__ == "__main__":
    main()
