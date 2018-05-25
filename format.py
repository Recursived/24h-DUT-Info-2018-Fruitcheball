from constants import *

class format(object):
	""" Objet de conversion des données envoyées du serveur """
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
			self.data[D_TEAMS][i][T_PLAYERS] = [[0, 0, P_EMPTY] for i in range(3)]
			self.data[D_TEAMS][i][T_FRUITS] = [0, 0, 0, 0, 0]
			self.data[D_TEAMS][i][T_ZONE] = None
			self.data[D_TEAMS][i][T_SCORE] = 0


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

		for playerLine in range(3, len(lst)):
			player = playerLine - 3
			bigLine = lst[playerLine].split(",")

			for coord in range(2, 5):
				coord = bigLine[coord].split(":")

				if coord[3] == "x":
					hold = P_EMPTY
				else:
					hold = int(coord[3])
				self.data[D_TEAMS][player][T_PLAYERS] = [int(coord[1]), int(coord[2]), hold]

			if self.data[D_TEAMS][player][T_ZONE] == None:
				coords = [0, 0, 0, 0, 0, 0]
				i = 0
				for coord in range(6, 9):
					coord = bigLine[coord].split(":")
					coords[i] = int(coord[1])
					coords[i+1] = int(coord[2])
					i += 2
				self.data[D_TEAMS][player][T_ZONE] = ((coords[0], coords[1]), (coords[2], coords[3]), (coords[4], coords[5]))

			self.data[D_TEAMS][player][T_SCORE] = int(bigLine[10])

			i = 0
			for coord in range(12, 17):
				coord = bigLine[coord].split(":")

				self.data[D_TEAMS][player][T_FRUITS][i] = int(coord[1])
				i += 1
		return self.data






		