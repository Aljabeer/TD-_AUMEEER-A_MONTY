#!/usr/bin/env python

import sys

def mul (x,y):
	return x*y

if __name__=="__main__":
        if ( len(sys.argv) >  3):
                print("Entrez que 2 variable")

        elif ( len(sys.argv) == 1 ):
                x = input("Premier valeur: ")
                y = input("Deuxieme valeur: ")
                x = int(x)
                y = int(y)
                print(mul(x,y))
        elif (len(sys.argv) == 2 ):
                print("Entrez encore une valeur")
                y = input("Le deuxieme valeur: ")
                x = int( sys.argv[1] )
                y = int(y)
                print(mul(x,y))
        else:
                x = int( sys.argv[1] )
                y = int( sys.argv[2] )
                print(mul(x,y))
