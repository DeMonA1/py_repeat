import zmq


host = '*'
port = 6789


context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.bind('tcp://%s:%s' % (host, port))

with open('../mammoth.txt', 'rt') as m:
    for line in m:
        data = m.readline()
        data = data.split(' ')
        for word in data:
            pub.send(word)