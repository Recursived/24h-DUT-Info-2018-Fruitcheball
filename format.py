from constants import *

class format(object):
	"""docstring for format"""
	def __init__(self, size, ident):
		pass
		self.mat = [None for i in range(size)]
		self.mat = [lst(self.mat) for i in range(size)]
		self.data = dict()

		self.data[D_MAP] = self.mat
		self.data[D_TEAMS] = [dict(), dict(), dict(), dict()]
		self.data[D_NUM_T] = int(ident)
		self.data[D_NUM_TURN] = 0

		for i in range(4):


	def fetchMessage(self, message):
		lst = message.split("_")

		self.data[D_NUM_TURN] = lst[0]

		nb = lst[1]

		grid = lst[2].split[","]
		i = 0
		for line in grid:
			cases = line.split("");
			j = 0
			for case in cases:
				if case == "X":
					self.mat[i][j] = M_WALL
				elif case == ".":
					self.mat[i][j] = M_EMPTY
				else:
					self.mat[i][j] = int(case);
				j += 1
			i += 1




		