import zmq, time


host = '*'
port = 6789


context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.bind('tcp://%s:%s' % (host, port))
time.sleep(1)
with open('../mammoth.txt', 'rt') as m:
    lines = m.readlines()
    for line in lines:
        data = line.split(' ')
        for word in data:
            pub.send_string(word)
            #pub.send_string(word)
            print('publish', word)