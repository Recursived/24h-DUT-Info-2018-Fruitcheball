

class format(object):
	"""docstring for format"""
	def __init__(self, size):
		pass
		self.mat = [None for i in range(size)]
		self.mat = [lst(self.mat) for i in range(size)]

	def fetchMessage(self, message):
		lst = message.split("_")
		current = lst[0]
		nb = lst[1]
		grid = lst[2].split[","]
		i = 0
		for line in grid:
			cases = line.split("");
			j = 0
			for case in cases:
				if case == "X":
					self.mat[i][j] = 


		