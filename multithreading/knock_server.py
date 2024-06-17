from typing import Optional
from twisted.internet import protocol, reactor
from twisted.internet.interfaces import IAddress
from twisted.internet.protocol import Protocol


class Knock(protocol.Protocol):
    def dataReceived(self, data: bytes) -> None:
        print ('Client:', data.decode('utf-8'))
        if data.startswith(b"Knock knock"):
            response = b"Who's there?"
        else:
            response = data + b" who?"
        print ('Server:', response)
        self.transport.write(response)


class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr: IAddress) -> Protocol | None:
        return Knock()
reactor.listenTCP(8000, KnockFactory())
reactor.run()