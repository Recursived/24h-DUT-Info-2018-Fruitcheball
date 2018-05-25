from constants import *

class Fetch(object):
	""" Objet de conversion des données envoyées du serveur """
	
	def __init__(self, ident):
		pass
		
		self.data = dict()
		self.mat = []
		self.written = False

		# Initialisation des entrées du dictionnaire data
		self.data[D_MAP] = []
		self.data[D_TEAMS] = []
		self.data[D_NUM_T] = int(ident)
		self.data[D_NUM_TURN] = 0


	def fetchMessage(self, message):
		# On décompose La trame en données
		lst = message.split("_")

		# On actualise le tour actuel
		self.data[D_NUM_TURN] = int(lst[0])

		# Si pas encore entierement initialisée
		if not self.written:
			size = int(lst[1])
			width, height = lst[2].split(",")[0].split(":")
			height = int(height)
			width = int(width)

			self.data[D_TEAMS] = [dict() for i in range(size)]

			# On définit les entrées du dictionnaire ne fontion du nombre de joeurs
			for i in range(size):
				self.data[D_TEAMS][i][T_PLAYERS] = [[0, 0, P_EMPTY] for i in range(3)]
				self.data[D_TEAMS][i][T_FRUITS] = [0, 0, 0, 0, 0]
				self.data[D_TEAMS][i][T_ZONE] = None
				self.data[D_TEAMS][i][T_SCORE] = 0

			# On initialise la matrice en fonction de sa taille
			self.mat = [None for i in range(width)]
			self.mat = [list(self.mat) for i in range(height)]
			self.data[D_MAP] = self.mat

		# on récupère les lignes de la carte (on retire ses dimensions)
		grid = lst[2].split(",")[1:]
		i = 0
		for line in grid:
			# On découpe les cases une a une
			cases = list(line)
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
			
			# On définit les coordonnées des joueurs
			i = 0
			for coord in range(2, 5):
				coord = bigLine[coord].split(":")

				if coord[3] == "x":
					hold = P_EMPTY
				else:
					hold = int(coord[3])

				self.data[D_TEAMS][player][T_PLAYERS][i] = [int(coord[1]), int(coord[2]), hold]
				i += 1

			if not self.written:
				print("passing in zone")
				coords = [0, 0, 0, 0, 0, 0]
				i = 0
				for coord in range(6, 9):
					coord = bigLine[coord].split(":")
					coords[i] = int(coord[1])
					coords[i+1] = int(coord[2])
					i += 2
				print(((coords[0], coords[1]), (coords[2], coords[3]), (coords[4], coords[5])))
				self.data[D_TEAMS][player][T_ZONE] = ((coords[0], coords[1]), (coords[2], coords[3]), (coords[4], coords[5]))

				self.written = True

			self.data[D_TEAMS][player][T_SCORE] = int(bigLine[10])

			i = 0
			for coord in range(12, 17):
				coord = bigLine[coord].split(":")

				self.data[D_TEAMS][player][T_FRUITS][i] = int(coord[1])
				i += 1
		return self.data






		