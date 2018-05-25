#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA codee par l equipe ascii_p<array>

# Imports ---------------------------------------------------------------------
import sys
from constants import *
from network import *
from fetch import *
from choiceAlea import alea
from direction import *

# Fonctions -------------------------------------------------------------------
def main():
	if len(sys.argv) == 2:
		ip = sys.argv[1]
		connexion = Network(ip)
	elif len(sys.argv) == 3:
		ip = sys.argv[1]
		port = sys.argv[2]
		connexion = Network(ip, port)
	else:
		connexion = Network()

	connexion.send("ascii_p<array>\n")
	numero = connexion.receive()
	dataFetching = Fetch(numero)
	lst = []

	while 1:
		received = connexion.receive()
		if received == "FIN\n":
			break
		data = dataFetching.fetchMessage(received)
		
		
		
		message = getReturnString(data)
		lst.append(data[D_TEAMS][data[D_NUM_T]][T_PLAYERS])
		if len(lst) > 2:
			lst.pop(0)
		
		if len(lst) == 2:
			if lst[0] == lst[1]:
				message = alea()
		
		# message = getReturnString(data)
		connexion.send(message)


if __name__ == '__main__':
    main()
