import socket
from datetime import datetime


address = ('localhost', 6789)
max_size = 4096


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(address)

data, client = server.recvfrom(max_size)
if data.decode('utf-8') == 'time':
    cloc = bytes(datetime.now().isoformat(), 'utf-8')
    server.sendto(cloc, client)
    server.close()
    