#/usr/bin/env python

def add_num(a,b):
	sum = a + b;
	return sum;

import sys
print("Bonjour, Bienvenue!!")


if __name__=="__main__":
        if ( len(sys.argv) >  3):
                print("Entrez que 2 variable")

        elif ( len(sys.argv) == 1 ):
                x = input("Premier valeur: ")
                y = input("Deuxieme valeur: ")
                x = int(x)
                y = int(y)
                print(add_num(x,y))
        elif (len(sys.argv) == 2 ):
                print("Entrez encore une valeur")
                y = input("Le deuxieme valeur: ")
                x = int( sys.argv[1] )
                y = int(y)
                print(add_num(x,y))
        else:
                x = int( sys.argv[1] )
                y = int( sys.argv[2] )
                print(add_num(x,y))
		
print("Mercii!!")    

