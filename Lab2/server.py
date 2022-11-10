import socket
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
    serverIP     = "127.0.0.1"
    serverPort   = 10500

    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    serverSocket.bind((serverIP, serverPort))
    print("The server is ready to receive")

    while(True):
        # obtain DNS query
        message, clientAddress = serverSocket.recvfrom(2048)

        clientMsg = message.decode()
        r = ' '.join(clientMsg[i:i+2] for i in range(0, len(clientMsg), 2))
        
        print("Request")
        print(r)

        # determine the id of the query and the domain name contained
        domain_name = get_user_input_from_header_and_body(clientMsg)
        id = clientMsg[:4]

        # send a reply to client
        dict_value = ip_dict[domain_name]
        res= create_header_and_body(domain_name, dict_value, id)
        r = ' '.join(res[i:i+2] for i in range(0, len(res), 2))

        print("Response")
        print(r)

        serverSocket.sendto(res.encode(), clientAddress)


if __name__ == "__main__":
    main()
