from math import log

fichier=open("nombres.txt")

i=0
maxi=0
gagnant=0
for ligne in fichier.readlines():
	i+=1
	tableau=ligne.split(",")
	candidat=log(float(tableau[0]))*float(tableau[1])
	if candidat>maxi:
		gagnant=i
		maxi=candidat

print gagnant,maxi
