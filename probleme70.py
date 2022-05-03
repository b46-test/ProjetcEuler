from math import sqrt


from euler import liste_premiers
from euler import chiffres

premiers=liste_premiers(10**7)
print len(premiers)

gagnant=10**7

for a in range(len(premiers)-1):
	if(premiers[a]*premiers[a+1]>10**7):
		break

	for b in range(a,len(premiers)):
		i=premiers[a]
		j=premiers[b]
		if i*j>10**7:
			break
		phi=i*j-j-i+1
		if chiffres(phi)==chiffres(i*j) and i*j/float(phi)<gagnant:
			gagnant=i*j/float(phi)
			ngagnant=i*j
			print "*",ngagnant,phi,gagnant


