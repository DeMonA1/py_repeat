import zmq, re 


host = '127.0.0.1'
port = 6789


context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.connect('tcp://%s:%s' % (host, port))
sub.setsockopt(zmq.SUBSCRIBE, b'')

while True:
    data = sub.recv()
    data = data.decode('utf-8')
    data = re.sub('[^A-Za-z0-9]+', '', data)
    if len(data) == 5:
        print(data)