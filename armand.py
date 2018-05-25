from constants import *

def findQuarterbacksWithNuts(data):
	""" Renvoie la position des quarterbacks avec une noix """
	lst = []
	for i in range(len(data[D_TEAMS])):
		if i == data[D_NUM_T]:
			continue
		quarter = data[D_TEAMS][i][T_PLAYERS][0]
		if quarter[2] == M_NUT:
			lst.append((quarter[0], quarter[1]))
	return lst

def haveFruit(data, numP):
	""" Renvoie si le joueur a un fruit """
	return data[D_TEAMS][data[D_NUM_T]][T_PLAYERS][numP] != P_EMPTY

def canThrowInBase(data, numP):
	""" Teste si le joueur peut lancer dans la base """
	player = data[D_NUM_T]
	zone = data[D_TEAMS][player][T_ZONE]
	pos = data[D_TEAMS][player][T_PLAYERS][numP]

	for case in zone:
		if case[0] == pos[0] and (-4 < case[1] - pos[1] < 4):
			return (case)
		if case[1] == pos[1] and (-4 < case[0] - pos[0] < 4):
			return (case)
	return False

def canThrowToCloserPlayer(data, numP):
	""" Teste si il peut lancer à un joueur plus proche de la base """
	team = data[D_NUM_T]
	freePlayers = []
	i = 0
	pos = data[D_TEAMS][player][T_PLAYERS][numP]
	for p in data[D_TEAMS][team][T_PLAYERS]:
		if i == numP:
			continue
		if p[2] == P_EMPTY:
			freePlayers.append(p)
		i += 1

	for free in freePlayers:
		if free[0] == pos[0] and (-4 < free[1] - pos[1] < 4):
			return True
			# if closerThanMe(data, free, pos):
			# 	return free
			return (free)
		if free[1] == pos[1] and (-4 < free[0] - pos[0] < 4):
			return True
			# if closerThanMe(data, free, pos):
			# 	return free
	return False

def closerThanMe(data, free, pos):
	""""""

def majorityFruit(data):
	""" Renvoie le fruit majoitaire """
	team = data[D_NUM_T]
	maxi = 0
	for i in range(5):
		if data[D_TEAMS][team][T_FRUITS][i] > maxi:
			maxi = i
	return maxi

def canMoveOn(data, i, j, numP):
	""" Verifie si le joueur peut bouger sur la case """
	players = []
	Cteam = data[D_NUM_T]
	pos = data[D_TEAMS][player][T_PLAYERS][numP][:2]
	numT = 0
	for team in data[D_TEAMS]:
		numA = 0
		for player in team[T_PLAYERS]:
			if i == Cteam and j == numP:
				continue
			if player[:2] == pos:
				return False
			numA += 1
		numT += 1
	return False
	
