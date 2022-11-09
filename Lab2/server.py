import socket
import random
from parsing import create_header_and_body, get_user_input_from_header_and_body

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

def main():
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

        domain_name = get_user_input_from_header_and_body(clientMsg)
        dict_value = ip_dict[domain_name]

        # Sending a reply to client
        res= create_header_and_body(domain_name, dict_value)
        r = ' '.join(res[i:i+2] for i in range(0, len(res), 2))
        print("Response")
        print(r)
        bytesToSend = bytearray.fromhex(res[2:])
        UDPServerSocket.sendto(bytesToSend, address)


if __name__ == "__main__":
    main()
