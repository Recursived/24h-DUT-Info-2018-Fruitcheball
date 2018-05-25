from network import Network

co = Network()
co.send("Test\n")
num = co.receive()

data = co.receive()