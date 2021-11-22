# Tutorial Youtube
# https://www.youtube.com/watch?v=4I9LEY-q-co&list=PLBOh8f9FoHHhvO5e5HF_6mYvtZegobYX2&index=6

# Usage
# 1) server - python dns.py
# 2) client - nslookup pippo.com 127.0.0.1

# RFC 1035
# https://www.ietf.org/rfc/rfc1035.txt
#                                     1  1  1  1  1  1
#       0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
#     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
#     |                      ID                       |
#     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
#     |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
#     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
#     |                    QDCOUNT                    |
#     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
#     |                    ANCOUNT                    |
#     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
#     |                    NSCOUNT                    |
#     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
#     |                    ARCOUNT                    |
#     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

import socket, glob, json

port = 53
ip = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

def load_zones():

    jsonzone = {}
    zonefiles = glob.glob('zones/*.zone')
    print(zonefiles)

    for zone in zonefiles:
        with open(zone) as zonedata:
            data = json.load(zonedata)
            zonename = data["$origin"]
            jsonzone[zonename] = data
    return jsonzone

zonedata = load_zones()

def getFlags(flags):

    byte1 = bytes(flags[:1])
    byte2 = bytes(flags[1:2])
    rflags = ''
    QR = '1'
    OPCODE = ''

    for bit in range(1,5):
        OPCODE += str(ord(byte1)&(1<<bit))  # bitwise operation (1<<bit genera un numero binario con l'uno a sinistra)

    AA = '1'
    TC = '0'
    RD = '0'
    RA = '0'
    Z = '000'
    RCODE = '0000'

    return int(QR+OPCODE+AA+TC+RD, 2).to_bytes(1, byteorder='big') + int(RA+Z+RCODE, 2).to_bytes(1, byteorder='big')

def getrecs(data):
    domain, questiontype = getquestiondomain(data)
    at = ''
    if questiontype == b'\x00\x01':
        qt = 'a'

    zone = getzone(domain)

    return (zone, qt, domainname)

def getquestiondomain(data):
    state = 0
    expectedlength = 0
    domainstring = ''
    domainparts = []
    x = 0
    y = 0
    
    for byte in data:
        if state == 1:
            if byte != 0:
                domainstring += chr(byte)
            x += 1
            if x == expectedlength:
                domainparts.append(domainstring)
                domainstring = ''
                state = 0
                x = 0
            if byte == 0:
                domainparts.append(domainstring)
                break

        else:
            state = 1
            expectedlength = byte

        y += 1

    questiontype = data[y+1:y+3]
    print(questiontype)

    return (domainparts, questiontype)

def getzone(domain):
    global zonedata

    zone_name = '.'.join(domain)
    return zonedata[zone_name]

def buildresponse(data):
    
    # Transaction ID
    TransactionID = data[:2]    # Get first 2 bytes (Transaction Id, vedi RFC)
    TID = ''
    for byte in TransactionID:
        TID += hex(byte)[2:] 
    
    # Get the Flags
    Flags = getFlags(data[2:4])

    # Question count
    QDCOUNT = b'\x00\x01'

    # Answer count
    print(getrecs(data[12:]))

while 1:
    data, addr = sock.recvfrom(512)
    r = buildresponse(data)
    sock.sendto(r, 'addr')