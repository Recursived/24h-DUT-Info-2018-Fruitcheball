#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA codee par l equipe ascii_p<array>

# Imports ---------------------------------------------------------------------
import sys
from constants import *
from network import *
from fetch import *

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

	data = connexion.receive()
	print(dataFetching.fetchMessage(data))


if __name__ == '__main__':
    main()