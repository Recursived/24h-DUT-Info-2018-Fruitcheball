#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA codee par l equipe ascii_p<array>

# Imports ---------------------------------------------------------------------
#import os
import sys
from constant import *
from network import *
from format import *

# Fonctions -------------------------------------------------------------------
def main():
	print(len(sys.argv))
	if len(sys.argv) = 2:
		ip = sys.argv[1]
		connexion = Network(ip)
	elif len(sys.argv) = 3:
		ip = sys.argv[1]
		port = sys.argv[2]
		connexion = Network(ip, port)
	else:
		connexion()
	


if __name__ == '__main__':
    main()