#/usr/bin/env python

def add_num(a,b):
	sum = a + b;
	return sum;

print("Bonjour, Bienvenue!!")
def main():
	import sys

	print(sys.argv)
	i = (len(sys.argv)-1)
	print(i)
	if(i == 1):
		x = int(input("Inserer un nombre svp: "))
		y = int(input("Inserer une autre valeur svp: "))

		print("La somme de", x, " + ", y, " est ", add_num(x,y))
	else:
		print("Erreurs; seulment deux arguemnts svp!!")
main()

print("Mercii!!")

