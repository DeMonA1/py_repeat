import zmq


host = '127.0.0.1'
port = 6789

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect('tcp://%s:%s' % (host, port))
clock = ''
while clock != 'time':
    clock = input('Write the command: ')
client.send(clock.encode('utf-8'))
data = client.recv()
print(data.decode('utf-8'))
client.close()