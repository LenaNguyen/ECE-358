from socket import *

SERVER_IP = '127.0.0.1'
SERVER_PORT = 10101

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

req = 'GET htdocs/NestedHelloWorld.html HTTP/1.0\r '
client_socket.send(req.encode())
resp = client_socket.recv(2048)
print('From Server: ', resp.decode())
client_socket.close()
