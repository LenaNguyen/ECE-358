import socket
import random

ip_dict = {
    "google.com" : {
        "Type" : "IN",
        "Class" : "A",
        "TTL" : 260,
        "IP address" : ['192.165.1.1', '192.165.1.10']
    },
    "youtube.com" : {
        "Type" : "IN",
        "Class" : "A",
        "TTL" : 160,
        "IP address" : ['192.165.1.2']
    },
    "uwaterloo.ca" : {
        "Type" : "IN",
        "Class" : "A",
        "TTL" : 160,
        "IP address" : ['192.165.1.3']
    },
    "wikipedia.org" : {
        "Type" : "IN",
        "Class" : "A",
        "TTL" : 160,
        "IP address" : ['192.165.1.4']
    },
    "amazon.ca" : {
        "Type" : "IN",
        "Class" : "A",
        "TTL" : 160,
        "IP address" : ['192.165.1.5']
    }
}

def create_header(query, answer):
    print(query)
    id = rand_key()

    # flags
    qr = '1'
    opcode = '0000'
    aa = '1'
    tc = '0'
    rd = '0'
    ra = '0'
    z = '000'
    rcode = '0000'

    # other
    qdcount = '0001'
    ancount = "{:04x}".format(len(answer['IP address']))
    nscount = '0000'
    arcount = '0000'

    rr = ''
    for ip in answer['IP address']:
        # answer
        name = 'c00c'
        type = '0001'
        clss = '0001'
        ttl = "{:08x}".format(answer['TTL'])
        rdlength = "{:04x}".format(4)            
        rr += name + type + clss + ttl + rdlength
        for num in ip.split('.'):
            rr += "{:02x}".format(int(num))


    return hex(int(id+qr+opcode+aa+tc+rd+ra+z+rcode, 2)) + qdcount + ancount + nscount + arcount + query + rr

def rand_key():
    key1 = ""
 
    for i in range(16):
        temp = str(random.randint(0, 1))
        key1 += (temp)
         
    return(key1)

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = message.hex()
    r = ' '.join(clientMsg[i:i+2] for i in range(0, len(clientMsg), 2))

    clientIP  = "Client IP Address:{}".format(address)
    
    print("Request")
    print(r)
    print(clientIP)

    body = clientMsg[24:]
    dom_len_octet = int(body[:2], 16)
    dom = body[2:2+2*dom_len_octet]
    org_len_octet = int(body[2+2*dom_len_octet:4+2*dom_len_octet], 16)
    org = body[4+2*dom_len_octet:4+2*dom_len_octet+2*org_len_octet]

    domain_name = bytes.fromhex(dom).decode('utf-8') + '.' + bytes.fromhex(org).decode('utf-8')
    dict_value = ip_dict[domain_name]

    # Sending a reply to client
    res= create_header(body, dict_value)
    r = ' '.join(res[i:i+2] for i in range(0, len(res), 2))
    print("Response")
    print(r)
    bytesToSend = bytearray.fromhex(res[2:])


    UDPServerSocket.sendto(bytesToSend, address)
