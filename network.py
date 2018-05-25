import socket

class Network:

	def __init__(self, ip="127.0.0.1", port=1337):
		self.ip = ip
		self.port = port
		self.sock = self._connectTo()
		
	def _connectTo(self):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((self.ip, self.port))
			return sock
		except:
			raise Exception("Unable to connect to this ip and port.")
			
	def receive(self):
		try:
			data = self.sock.recv(2048)
		
		except:                                   # Si la connection est morte
			# recreate the socket and reconnect
			self.sock = self._connectTo()
			data = self.sock.recv(2048)
			
		return data.decode()
		
	def send(self, data):
		data = data.encode()
		
		try:
			self.sock.send(data)
		
		except:                                   # Si la connection est morte
			# recreate the socket and reconnect
			self.sock = self._connectTo()
			self.sock.send(data)
	
			