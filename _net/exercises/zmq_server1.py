import zmq
import datetime


host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind('tcp://%s:%s' % (host, port))
data = server.recv()
if data.decode('utf-8') == 'time':
    server.send(bytes(datetime.datetime.now().isoformat(), 'utf-8'))
    server.close()