""" Fichier contenant toutes les constantes du jeu. """

############# Constantes de la matrice ##############

M_WALL = -1     # Mur
M_EMPTY = None  # Vide
M_NUT = 4       # Chataigne

############# Constantes du dico de data ##############

D_TEAMS = "teams"  					# Clé correspondant à la liste des différents dico d'équipes de la partie
D_MAP = "map"      					# Clé correspondant à la matrice du jeu
D_NUM_T = "numT"   					# Clé correspondant au numéro de notre équipe
D_NUM_TURN = "numTurn"              # Clé correspondant au numéro du tour courrant


############# Constantes du dico d'une team ##############

T_PLAYERS = "players"               # Clé correspondant à la liste des différents joueurs (indice 0 : quater, indice 1 : lanceur1, indice 2 : lanceur 2)
T_FRUITS = "fruits"                 # Clé correspondant à la liste de quantité de fruits possédé par l'équipe
T_ZONE = "zone"                     # Clé correspondant au tuple contenant les tuples de coord des cases de la zone de l'équipe
T_SCORE = "score"                   # Clé correspondant au score de l'équipe

