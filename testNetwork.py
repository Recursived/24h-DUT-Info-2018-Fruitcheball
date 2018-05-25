from network import Network
from fetch import Fetch

co = Network()
co.send("Test\n")
num = co.receive()
dataFetching = Fetch(13, num)

data = co.receive()
print(dataFetching.fetchMessage(data))
