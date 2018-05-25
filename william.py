from constants import *
from maneta import *
from direction
from armand import *


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
				
				case = data[D_TEAMS][myTeamNum][T_ZONE][0]
				path = getPathToCoord(thisPlayer, case, data[D_MAP])
				return getDirection(thisPlayer, path, data)
				
		else:   # Si la position ou il est dangereuse
			case = data[D_TEAMS][myTeamNum][T_ZONE][0]
			path = getPathToCoord(thisPlayer, case, data[D_MAP])
			return getDirection(thisPlayer, path, data)
			
			
	else:   # Si le joueur n'a pas de fruits sur lui
		
		if not positionIsDangerous(data, thisPlayer[0], thisPlayer[1]):
			
			if isOnFruit(data, numPlayer):
				return "P"
		
		# elif fruitInMajorityNotFar():
			# y aller de manière non dangereuse
			
		else:
			case = getNearestFruit((thisPlayer[0], thisPlayer[1]), getFruits(data[D_MAP]))
			path = getPathToCoord(thisPlayer, case, data[D_MAP])
			return getDirection(thisPlayer, path, data)
			
	
			
	def chooseQuarter(data, numPlayer):
		thisPlayer = data[D_TEAMS][myTeamNum][T_PLAYERS][numPlayer]
		
		if thisPlayer[2] == M_NUT:    # Si le quater a une chataigne
			
			case = enemyAligned(data, thisPlayer[0], thisPlayer[1])
			if case:
				path = getPathToCoord(thisPlayer, case, data[D_MAP])
				return "L" + getDirection(thisPlayer, path, data)
			
			case = enemyBaseAligned(data, thisPlayer[0], thisPlayer[1]):
			elif case:
				path = getPathToCoord(thisPlayer, case, data[D_MAP])
				return "L" + getDirection(thisPlayer, path, data)
				
			else:
				case = getNearestFruit((thisPlayer[0], thisPlayer[1]), getEnemies(data))
				path = getPathToCoord(thisPlayer, case, data[D_MAP])
				return getDirection(thisPlayer, path, data)
				
				
		elif thisPlayer[2] != P_EMPTY:
			return choosePlayer(data, numPlayer)
		
		else:
			case = getNearestFruit((thisPlayer[0], thisPlayer[1]), getNuts(data))
			path = getPathToCoord(thisPlayer, case, data[D_MAP])
			return getDirection(thisPlayer, path, data)
			
		
		
	