import zmq,re 


host = '127.0.0.1'
port = 6789


context = zmq.Context()
client = context.socket(zmq.SUB)
client.connect('tcp://%s:%s' % (host, port))

sub = client.setsockopt(zmq.SUBSCRIBE, b'')