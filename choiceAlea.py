SEPARATOR = "-"
from random import randint

def alea():
	msg = ""
	
	for i in range(3):
		j = 1
		
		if j == 1:
			x = randint(1, 5)
			
			if x == 1:
				m = "N"
			elif x == 2:
				m = "E"
			elif x == 3:
				m = "O"
			elif x == 4:
				m = "S"
			else:
				m = "X"
			
		elif j == 2:
			m = "P"
			
		else:
			x = randint(1, 4)
			
			if x == 1:
				m = "LN"
			elif x == 2:
				m = "LE"
			elif x == 3:
				m = "LO"
			else:
				m = "LS"
		
		sep = SEPARATOR if i < 2 else "\n"
		msg += m + sep
	
	return msg
			