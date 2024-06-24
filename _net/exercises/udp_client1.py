import socket



address = ('localhost', 6789)
max_size = 4096


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clock = ''
while clock != 'time':
    clock = input('Input "time" for receiving current time: ')
clock = bytes(clock, 'utf-8')
client.sendto(clock, address)
data, server = client.recvfrom(max_size)
print('The current time: ', data.decode('utf-8'))
client.close()
