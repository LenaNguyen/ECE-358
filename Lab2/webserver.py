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


while True:
    connection_socket, addr = server_socket.accept()
    request = connection_socket.recv(2048).decode()
    headers = request.split("\n")
    path = headers[0].split()[1]
    if path[0] == '/':
        path = path[1:]

    try:
        print("A")
        print(headers)
        print(path)

        file = open(path)
        content = file.read()
        file.close()
        mod_datetime = get_modified_datetime(path)

        resp = 'HTTP/1.0 200 OK\n' + \
            'Date: {}\n'.format(date.today()) + \
            'Server: {}\n'.format(gethostname()) + \
            'Last-Modified: {}\n'.format(mod_datetime) + \
            'Content-Length: {}\n'.format(len(content)) + \
            'Content-Type: {}\n'.format('text/html') + \
            'Connection: Closed' + \
            '\n\n' + content

    except FileNotFoundError:
        content = 'File Not Found'
        resp = 'HTTP/1.0 404 NOT FOUND\n' +\
            'Date: {}\n'.format(date.today()) + \
            'Server: {}\n'.format(gethostname()) + \
            'Content-Length: {}\n'.format(len(content)) + \
            'Content-Type: {}\n'.format('text/html') + \
            'Connection: Closed' + \
            '\n\n' + content

    connection_socket.send(resp.encode())
    connection_socket.close()
