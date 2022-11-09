import socket
import random
import re
from parsing import create_header_and_body, get_user_input_from_header_and_body

def parse_response(msgFromServer):
    domain_name = get_user_input_from_header_and_body(msgFromServer)
    rr = msgFromServer.split('c00c')
    rr.pop(0)

    for r in rr:
        indices = [0,4,8,16,20]
        parts = [r[i:j] for i,j in zip(indices, indices[1:]+[None])]
        type = get_type(int(parts[0],16))
        clss = "IN" if int(parts[1], 16) else ""
        ttl = int(parts[2], 16)
        length = int(parts[3], 16)
        msg = get_ip(parts[4])
        print("{}: type {}, class {}, TTL {}, addr ({}) {}".format(domain_name,type,clss,ttl,length,msg))    


def get_type(type):
    if type == 1:
        return "A"
    if type == 2:
        return "NS"
    else:
        return "MX"

def get_ip(msg):
    ip = re.findall('..',msg)
    ip_addr = []
    for i in ip:
        ip_addr.append(str(int(i, 16)))
    return '.'.join(ip_addr)


def main():
    serverAddressPort   = ("127.0.0.1", 20001)
    bufferSize          = 1024

    while True:
        user_input = input('Enter Domain Name: ')

        if user_input == 'end':
            break

        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        query = create_header_and_body(user_input)
        UDPClientSocket.sendto(bytearray.fromhex(query), serverAddressPort)

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)[0].hex()
        parse_response(msgFromServer)
        
    print("Session ended")


if __name__ == "__main__":
    main()