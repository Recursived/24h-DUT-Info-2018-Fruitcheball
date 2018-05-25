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
			return True
		if case[1] == pos[1] and (-4 < case[0] - pos[0] < 4):
			return True
	return False

def canThrowToCloserPlayer(data, numP):
	""" 
