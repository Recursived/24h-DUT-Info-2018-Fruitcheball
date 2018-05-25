from network import Network
from fetch import Fetch

co = Network()
co.send("Test\n")
num = co.receive()
dataFetching = Fetch(num)

data = co.receive()
print(dataFetching.fetchMessage(data))
