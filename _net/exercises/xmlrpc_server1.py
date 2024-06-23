from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime


def clock():
    return datetime.now().isoformat()

server = SimpleXMLRPCServer(('localhost', 6789))
server.register_function(clock, 'clock')
server.serve_forever()