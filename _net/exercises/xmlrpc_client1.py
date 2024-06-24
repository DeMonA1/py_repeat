from xmlrpc.client import ServerProxy


proxy = ServerProxy('http://localhost:6789/')
command = ''
while command != 'time':
    command = input('Write the command: ')
print(proxy.clock())