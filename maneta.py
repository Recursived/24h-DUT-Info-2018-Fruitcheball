import maneta as ma
import armand as ar
from constants import *

def positionIsDangerous(data,i,j):
	"""
	Cette fonction renvoie true si la position est
	sinon false

	"""
	lst_nuts = ar.findQuarterbacksWithNuts(data)
	threatened = False
	map1 = data[D_MAP]
	l = len(map1)
	# verification de la ligne supérieure
	for i in range(1,5):
		if (posi - i, j) in lst_nuts and (0 < posi - i < l and	0 < j < l):
			threatened = True
	#verification de la ligne inférieure
	for i in range(1,5):
		if (posi + i, j) in lst_nuts and (0 < posi + i < l and	0 < j < l):
			threatened = True
	#verification de des éléments à gauche
	for j in range(1,5):
		if (i,posj - j)	 in lst_nuts and (0 < i < l and	 0 < posj-j < l):
			threatened = True
	#verification de des éléments à droite
	for j in range(1,5):
		if (i,posj + j) in lst_nuts and (0 < i< l and  0 < posj - j < l):
			threatened = True

	return threatened

def getNeighboursDangerous(data,i,j):
	"""
	retourne une liste bas->gauche->droite->haut de booléen
	"""
	surround = [(posi+1,posj),(posi,posj-1),(posi,posj+1),(posi-1,posj)]
	to_return = list()
	l = len(data[D_MAP])
	for k, m in surround:
		if 0 < k < l and 0 < m < l:
			to_return.append(positionIsDangerous(data,k,m))
	return to_return

def moveToSafe(data,i,j):
		safeList = ma.getNeighboursDangerous(i,j,data)
		bi, bj = data[D_TEAMS][data[D_NUM_T]][T_PLAYERS][numPlayer][T_ZONE][0]
		if bi<i and bj<j:
				if safeList[3]==True:
						return "N"
				elif safeList[1]==True:
						return "O"
				elif safeList[0]==True:
						return "S"
				else:
						return "E"
				
		elif bi<i and bj>j:
				if safeList[0]==True:
						return "S"
				elif safeList[1]==True:
						return "O"
				elif safeList[2]==True:
						return "E"
				else:
						return "N"


		elif bi>i and bj>j:
				if safeList[0]==True:
						return "S"
				elif safeList[2]==True:
						return "E"
				elif safeList[1]==True:
						return "O"
				else:
						return "N"

		else:
				if safeList[3]==True:
						return "N"
				elif safeList[2]==True:
						return "E"
				elif safeList[0]==True:
						return "S"
				else:
						return "O"

	def fruitOnCase(data,i,j):
		if data[D_MAP][i][j]!=None:
			if 0<=data[D_MAP][i][j]<=3:
				return True
			else:
				return False
		else:
			return False


	

if __name__ == '__main__':
	positionIsDangerous(5,5,[])
