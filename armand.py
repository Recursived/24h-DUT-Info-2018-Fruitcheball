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
