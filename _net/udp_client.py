import socket
from datetime import datetime

server_adress = ('localhost', 6789)
max_size = 4096

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Hey!', server_adress)
data, server = client.recvfrom(max_size)
print('At', datetime.now(), server, 'said', data)
client.close()