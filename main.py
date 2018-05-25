#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA codee par l equipe ascii_p<array>

# Imports ---------------------------------------------------------------------
#import os
import sys
from network import *

# Fonctions -------------------------------------------------------------------
def main():
	print(len(sys.argv))
	ip = sys.argv[1]
	if len(sys.argv) > 2:
		port = sys.argv[2]
	else:
		port = 1337
	connexion = Network(ip, port)


if __name__ == '__main__':
    main()