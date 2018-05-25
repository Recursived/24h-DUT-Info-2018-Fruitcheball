from constants import *
from maneta import *
from direction
from armand import *

def throwInBase

def choosePlayer(data, numPlayer):
	
	myTeamNum = data[D_NUM_T]
	thisPlayer = data[D_TEAMS][myTeamNum][T_PLAYERS][numPlayer]
	thisPlayerCoords = (thisPlayer[0], thisPlayer[1])
	
	notToGo = getNeighboursDangerous(data, thisPlayer[0], thisPlayer[1])
	
	if thisPlayer[2] != P_EMPTY:    # Si le joueur a un fruit sur lui
		
		if not positionIsDangerous(data, thisPlayer[0], thisPlayer[1]):    # Si le joueur n'est pas sur une pos dangereuse
			
			case = canThrowInBase(data, numPlayer)
			if case:
				path = getPathToCoord(thisPlayer, case, data[D_MAP])
				return "L" + getDirection(thisPlayer, path, data)
			
			case = canThrowToCloserPlayer(data, numPlayer)
			elif case:
				path = getPathToCoord(thisPlayer, case, data[D_MAP])
				return "L" + getDirection(thisPlayer, path, data)
				
			else:
				
				# Se deplacer vers la base de manière non dangereuse
				
		else:   # Si la position ou il est dangereuse
			# Bouger obligatoirement de manière non dangereuse vers la base
			
	else:   # Si le joueur n'a pas de fruits sur lui
		
		if not positionIsDangerous(data, thisPlayer[0], thisPlayer[1]):
			
			if isOnFruit(data, numPlayer):
				return "P"
		
		# elif fruitInMajorityNotFar():
			# y aller de manière non dangereuse
			
		else:
			case = getNearestFruit((thisPlayer[0], thisPlayer[1]), getFruits(data[D_MAP]))
			
	
			
	def chooseQuarter(data, numPlayer):
		thisPlayer = data[D_TEAMS][myTeamNum][T_PLAYERS][numPlayer]
		
		if thisPlayer[2] == M_NUT:    # Si le quater a une chataigne
			
			if ennemyAligned(thisPlayer[0], thisPlayer[1]):
				# On lui lance dessus
			elif baseEnnemyAligned(thisPlayer[0], thisPlayer[1]):
				# On lui lance dessus
			else:
				# Se deplacer vers ennemi le plus proche
				
		elif thisPlayer[2] != P_EMPTY:
			return choosePlayer(data, numPlayer)
		
		else:
			# va chercher la chataigne la plus prochye
			
		
		
	