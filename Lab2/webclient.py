from socket import *
import argparse

SERVER_IP = '127.0.0.1'
SERVER_PORT = 10101


def make_request(req):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    client_socket.send(req.encode())
    resp = client_socket.recv(2048)
    print(resp.decode())
    client_socket.close()


def get_file():
    print("Fetching file...")
    req = 'GET HelloWorld.html HTTP/1.0\r '
    make_request(req)
    print("\n")


def head_file():
    print("Fetching headers for file...")
    req = 'HEAD HelloWorld.html HTTP/1.0\r '
    make_request(req)
    print("\n")


def get_nested_file():
    print("Fetching nested file...")
    req = 'GET htdocs/NestedHelloWorld.html HTTP/1.0\r '
    make_request(req)
    print("\n")


def head_nested_file():
    print("Fetching headers for nested file...")
    req = 'HEAD htdocs/NestedHelloWorld.html HTTP/1.0\r '
    make_request(req)
    print("\n")


def get_file_not_found():
    print("Fetching unknown file...")
    req = 'GET World.html HTTP/1.0\r '
    make_request(req)
    print("\n")


def head_file_not_found():
    print("Fetching headers for unknown file...")
    req = 'HEAD World.html HTTP/1.0\r '
    make_request(req)
    print("\n")


def run_get_requests():
    print("**GET REQUESTS**")
    get_file()
    get_nested_file()
    get_file_not_found()


def run_head_requests():
    print("**HEAD REQUESTS**")
    head_file()
    head_nested_file()
    head_file_not_found()


def main():
    parser = argparse.ArgumentParser(description='ECE 358 Lab 2 Task 1')
    parser.add_argument('-get', '--get', action='store_true',
                        help='Execute GET requests')
    parser.add_argument('-head', '--head', action='store_true',
                        help='Execute HEAD requests')

    args = parser.parse_args()
    if args.get:
        run_get_requests()
        exit()
    elif args.head:
        run_head_requests()
        exit()


if __name__ == "__main__":
    main()
