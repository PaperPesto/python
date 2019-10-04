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

import socket

port = 53
ip = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

def getFlags(flags):

    byte1 = bytes(flags[:1])
    byte2 = bytes(flags[1:2])
    rflags = ''
    QR = '1'
    OPCODE = ''
    for bit in range()

def buildresponse(data):
    
    # Transaction ID
    TransactionID = data[:2]    # Get first 2 bytes (Transaction Id, vedi RFC)
    TID = ''
    for byte in TransactionID:
        TID += hex(byte))[2:]
    
    # Get the Flags
    Flags = getFlags(data[2:4])

while 1:
    data, addr = sock.recvfrom(512)
    r = buildresponse(data)
    sock.sendto(r, 'addr')