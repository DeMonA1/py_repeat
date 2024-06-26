from twisted.internet import reactor, protocol

b = "Knock knock".encode('utf-8')
class KnockClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(b)
    
    def dataReceived(self, data: bytes) -> None:
        if data.startswith(b"Who's there?"):
            response = b"Disappearing client"
            self.transport.write(response)
        else:
            self.transport.loseConnection()
            reactor.stop()
    

class KnockFactory(protocol.ClientFactory):
    protocol = KnockClient


def main():
    f = KnockFactory()
    reactor.connectTCP('localhost', 8000, f)
    reactor.run()

if __name__ == '__main__':
    main()