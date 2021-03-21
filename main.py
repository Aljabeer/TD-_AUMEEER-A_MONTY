from addTwoIntc import add_num
from mulTwoInt import mul
z= " "
z = input("Choisi entre A pour additioner ou M multiplier: ")
while ((z == "A") or (z == "M")):
	if (z =="A"):
		a = input("Pour additionner appuyer y ou pour sortir appuyer q: ")
		while((a=="y") or (a=="q")):
			if (a=="y"):
				a = input("Entrez le premier valeur: ")
				b = input("Entrez le deuxieme valeur: ")
				a = int(a) 
				b = int(b)
				print(add_num(a,b))
				break
			elif (a=="q"):
				break
			else:
				print("error!!")
	elif (z=="M"):
		b = input("Pour multipliyer appuyer y ou pour sortir appuyer q:")
		while((b=="y") or (b=="q")):
			if (b=="y"):
				d=input("Premier valeur svp: ")
				e=input("Deuxieme valeur svp: ")
				d=int(d)
				e=int(e)
				print(mul(d,e))
				break
			elif (b=="q"):
				break
			else: 
				print("error!!")
	else:
		print("Rechoisi entre A ou M")
