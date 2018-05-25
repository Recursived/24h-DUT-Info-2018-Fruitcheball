from constants import *

# Node : (x,y,cost,heuristic,parent)

def compareHeuristic(node1, node2):
	if node1[3] < node2[3]:
		return 1
	if node1[3] == node2[3]:
		return 0
	return -1


def getNeighboors(graph, node):
	x,y = node[0],node[1]
	last = graph[-1][-1]
	width,height = last[0],last[1]
	neighboors = []
	if (x-1) >= 0: neighboors.append(graph[x-1][y])
	if (x+1) <= width: neighboors.append(graph[x+1][y])
	if (y-1) >= 0: neighboors.append(graph[x][y-1])
	if (y+1) <= height: neighboors.append(graph[x][y+1])
	return neighboors

def distanceToNode(start,end):
	return abs(start[0]-end[0]) + abs(start[1]-end[1])

def buildWay(start, objective):
	daWae = []
	u = objective
	while u != start:
		daWae.append((u[0],u[1]))
		u = u[4]
	daWae.reverse()
	return daWae

def shortestWay(graph, start, objective):
	#Initialization
	closedList = []
	openList = []
	openList.append(start)
	#Execution
	while openList:
		u = openList.pop(0)
		if (u[0] == objective[0]) and (u[1] == objective[1]):
			return buildWay(start,objective)
		for v in getNeighboors(graph,u):
			if (v in closedList) or ((v in openList) and v[2]<u[2]+1) or (v[4]==-1): continue # or (v[4]==-1)
			v[4] = u #Setting parent to u
			v[2] = u[2]+1 #Updating cost
			v[3] = v[2]+distanceToNode(u,v) #Updating heuristic
			openList.append(v)
		closedList.append(u)
		#~ openList = sorted(openList, key=lambda node: mergeSort())
		openList = sorted(openList, key=lambda node: node[3])
	
def initializeGraph(struct):
	graph = []
	height = len(struct)
	width = len(struct[0])
	for j in range(height):
		graph.append([])
		for i in range(width):
			valeur = 0
			if struct[j][i] and struct[j][i] == -1:
				valeur = -1
			graph[j].append([j,i,0,0,valeur])
	return graph



def getFruits(struct):
	fruits = []
	height = len(struct)
	width = len(struct[0])	
	for j in range(height):
		for i in range(width):
			if struct[j][i] and 0 <= struct[j][i] < 4:
				fruits.append((j,i))
	return fruits

def getNearestFruit(pos, fruits):
	dist = dict()
	for fruit in fruits:
		dist[fruit] = abs(fruit[0]-pos[0]) + abs(fruit[1]-pos[1])
	return sorted(dist, key=lambda fruit: dist[fruit])[0]
	
def getPathToCoord(player, fruit, struct):
	graph = initializeGraph(struct)
	playerNode = graph[player[0]][player[1]]
	fruitNode = graph[fruit[0]][fruit[1]]
	return shortestWay(graph,playerNode,fruitNode)
	
def getDirection(player, path, data):
	"""Get direction to go from player to nearest fruit"""
	pos1 = (player[0],player[1])
	pos2 = path[0]
	if pos1[0] == pos2[0]:
		if pos1[1] > pos2[1]:
			return "E"
		return "O"
	if pos1[0] > pos2[0]:
		return "S"
	return "N"
	
	
def getChoice(player,fruits, data):
	
	pos = (player[0],player[1])
	team = data[D_TEAMS][data[D_NUM_T]]
	print(team)
	if player[2]: #si tient quelque chose
		if pos in team[T_ZONE]: #si dans sa zone
			return "P"  #lache le fruit
		#retourne à la base
		return getDirection(player,getPathToCoord(player,data[D_TEAMS][T_ZONE][1],data[D_MAP]),data) #rentre à la base
	if data[D_MAP][pos[1]][pos[0]] and (0 <= data[D_MAP][pos[1]][pos[0]] < 4): #si sur un fruit
		return "P" #prend le fruit
	fruit = getNearestFruit(pos,fruits) #sinon va vers fruit le plus proche
	fruits.remove(fruit)
	print("fruit:")
	print(fruit)
	return getDirection(player, getPathToCoord(player, fruit, data[D_MAP]), data)
	
	

def getReturnString(data):
	team = data[D_TEAMS][data[D_NUM_T]]
	fruits = getFruits(data[D_MAP])
	players = team[T_PLAYERS]
	return getChoice(players[0],fruits,data)+"-"+getChoice(players[1],fruits,data)+"-"+getChoice(players[2],fruits,data)+"\n"
		
	

if __name__=="__main__":
	pass
