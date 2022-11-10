from socket import *
from datetime import date
import os
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT = 10101

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)

print("The server is ready to receive")


def get_modified_datetime(path):
    seconds = os.path.getmtime(path)
    return time.ctime(seconds)


def generate_headers(status_code, content_length, path):
    mod_datetime = get_modified_datetime(path)
    status = "HTTP/1.0 200 OK\n" if status_code == 200 else "HTTP/1.0 404 NOT FOUND\n"
    return status + \
        'Date: {}\n'.format(date.today()) + \
        'Server: {}\n'.format(gethostname()) + \
        'Last-Modified: {}\n'.format(mod_datetime) + \
        'Content-Length: {}\n'.format(content_length) + \
        'Content-Type: {}\n'.format('text/html') + \
        'Connection: close'


while True:
    connection_socket, addr = server_socket.accept()
    request = connection_socket.recv(2048).decode()
    headers = request.split("\n")
    header_vals = headers[0].split()

    if len(header_vals) > 1:
        path = header_vals[1]
        method = header_vals[0]
        if path[0] == '/':
            path = path[1:]

    if path:
        try:
            file = open(path)
            content = file.read()
            file.close()
            resp = generate_headers(200, len(content), path)
            if method == "GET":
                resp += '\n\n' + content

        except FileNotFoundError:
            path = "NotFound.html"
            file = open(path)
            content = file.read()
            file.close()

            resp = generate_headers(404, len(content), path)

            if method == "GET":
                resp += '\n\n' + content

        connection_socket.send(resp.encode())

    connection_socket.close()
