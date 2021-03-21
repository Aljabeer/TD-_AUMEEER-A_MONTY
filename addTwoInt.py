#/usr/bin/env python

def add_num(a,b):
	sum = a + b
	return sum

print("Bonjour, Bienvenue!!")

x = int(input("Inserer un nombre svp: "))
y = int(input("Inserer une autre valeur svp: "))

print("La somme de", x, " + ", y, " est ", add_num(x,y))

print("Mercii!!")
