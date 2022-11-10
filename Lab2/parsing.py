import random

def create_header_and_body(query, answer=None, id=None):
    id = "{:04x}".format(int(rand_id(),2)) if id is None else id

    # flags
    qr = '0' if answer is None else '1'
    opcode = '0000'
    aa = '1'
    tc = '0'
    rd = '0'
    ra = '0'
    z = '000'
    rcode = '0000'
    flags = "{:04x}".format(int(qr+opcode+aa+tc+rd+ra+z+rcode, 2))

    # other
    qdcount = "{:04x}".format(1)
    ancount = "{:04x}".format(0) if answer is None else "{:04x}".format(len(answer['IP address']))
    nscount = "{:04x}".format(0)
    arcount = "{:04x}".format(0)

    # query
    a = query.split('.')[0]
    b = query.split('.')[1]
    qname = "{:02x}".format(len(a)) + a.encode().hex() + "{:02x}".format(len(b)) + b.encode().hex() + "{:02x}".format(0)
    qtype = "{:04x}".format(1)
    qclass = "{:04x}".format(1)

    # answer
    rr = ''
    if answer is not None:
        for ip in answer['IP address']:
            name = 'c00c'
            type = "{:04x}".format(1)
            clss = "{:04x}".format(1)
            ttl = "{:08x}".format(answer['TTL'])
            rdlength = "{:04x}".format(4)            
            rr += name + type + clss + ttl + rdlength
            for num in ip.split('.'):
                rr += "{:02x}".format(int(num))

    resp = id + flags + qdcount + ancount + nscount + arcount + qname + qtype + qclass + rr
    return resp


def rand_id():
    id = ""
 
    for i in range(16):
        temp = str(random.randint(0, 1))
        id += (temp)
         
    return id


def get_user_input_from_header_and_body(msg):
    # it is known the header accounts for the first 24 values, the first values in the body is QNAME
    body = msg[24:]
    main_len_octet = int(body[:2], 16)
    main = body[2:2+2*main_len_octet]
    sec_len_octet = int(body[2+2*main_len_octet:4+2*main_len_octet], 16)
    sec = body[4+2*main_len_octet:4+2*main_len_octet+2*sec_len_octet]

    # obtain the string representation of the domain name
    domain_name = bytes.fromhex(main).decode('utf-8') + '.' + bytes.fromhex(sec).decode('utf-8')
    return domain_name
