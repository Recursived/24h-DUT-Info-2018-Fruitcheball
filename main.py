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

	while 1:
		received = connexion.receive()
		if received == "FIN\n":
			break
		data = dataFetching.fetchMessage(received)
		
		message = getReturnString(data)

		m = str()
		for i in range(3):
			if i == 0:
				m += chooseQuarter(data, i)
			else:
				m += choosePlayer(data, i)
			if i != 2:
				m += "-"
			else:
				m += "\n"

		# message = getReturnString(data)
		print(message)
		connexion.send(message)


if __name__ == '__main__':
    main()
