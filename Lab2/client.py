import socket
import random
import re


def create_header(query):
    id = rand_key()

    # flags
    qr = '0'
    opcode = '0000'
    aa = '1'
    tc = '0'
    rd = '0'
    ra = '0'
    z = '000'
    rcode = '0000'

    # other
    qdcount = '0001'
    ancount = '0000'
    nscount = '0000'
    arcount = '0000'

    # query
    a = query.split('.')[0]
    b = query.split('.')[1]
    qname = "{:02x}".format(len(a)) + a.encode().hex() + "{:02x}".format(len(b)) + b.encode().hex() + format(0, '02x')
    qtype = '0001'
    qclass = '0001'

    return hex(int(id+qr+opcode+aa+tc+rd+ra+z+rcode, 2)) + qdcount + ancount + nscount + arcount + qname + qtype + qclass


    # end flags
def rand_key():
    key1 = ""
 
    for i in range(16):
        temp = str(random.randint(0, 1))
        key1 += (temp)
         
    return(key1)

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

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

while True:
    user_input = input('Enter Domain Name: ')

    if user_input == 'end':
        break

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    res = create_header(user_input)
    r = ' '.join(res[i:i+2] for i in range(0, len(res), 2))
    UDPClientSocket.sendto(bytearray.fromhex(res[2:]), serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)[0].hex()
    r = ' '.join(msgFromServer[i:i+2] for i in range(0, len(msgFromServer), 2))
    msgFromServer
  
    body = msgFromServer[24:]
    dom_len_octet = int(body[:2], 16)
    dom = body[2:2+2*dom_len_octet]
    org_len_octet = int(body[2+2*dom_len_octet:4+2*dom_len_octet], 16)
    org = body[4+2*dom_len_octet:4+2*dom_len_octet+2*org_len_octet]

    domain_name = bytes.fromhex(dom).decode('utf-8') + '.' + bytes.fromhex(org).decode('utf-8')
    rr = body.split('c00c')
    rr.pop(0)

    for r in rr:
        print(r)
        indices = [0,4,8,16,20]
        parts = [r[i:j] for i,j in zip(indices, indices[1:]+[None])]
        type = get_type(int(parts[0],16))
        clss = "IN" if int(parts[1], 16) else ""
        ttl = int(parts[2], 16)
        length = int(parts[3], 16)
        msg = get_ip(parts[4])
        print(msg)
        print("{}: type {}, class {}, TTL {}, addr ({}) {}".format(domain_name,type,clss,ttl,length,msg))    

print("Session ended")
