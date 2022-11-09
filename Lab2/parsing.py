import random

def create_header_and_body(query, answer=None):
    id = rand_key()

    # flags
    qr = '0' if answer is None else '1'
    opcode = '0000'
    aa = '1'
    tc = '0'
    rd = '0'
    ra = '0'
    z = '000'
    rcode = '0000'

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

    resp = hex(int(id+qr+opcode+aa+tc+rd+ra+z+rcode, 2)) + qdcount + ancount + nscount + arcount + qname + qtype + qclass + rr
    return resp[2:]


def rand_key():
    id = ""
 
    for i in range(16):
        temp = str(random.randint(0, 1))
        id += (temp)
         
    return id


def get_user_input_from_header_and_body(msg):
    body = msg[24:]
    dom_len_octet = int(body[:2], 16)
    dom = body[2:2+2*dom_len_octet]
    org_len_octet = int(body[2+2*dom_len_octet:4+2*dom_len_octet], 16)
    org = body[4+2*dom_len_octet:4+2*dom_len_octet+2*org_len_octet]

    domain_name = bytes.fromhex(dom).decode('utf-8') + '.' + bytes.fromhex(org).decode('utf-8')
    return domain_name
