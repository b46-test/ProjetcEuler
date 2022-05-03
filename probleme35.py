from euler import chiffres
from euler import premiers
#from numarray import zeroes

limite=10**6
print limite
somme=0

liste=premiers(limite)

for i in range(limite):
	if liste[i]:
		reussi=True
		rot=int(str(i)[-1]+str(i/10))
		while reussi==True and rot!=i:
			if not liste[rot]:
				reussi=False
			rot=int(str(rot)[-1]+str(rot/10))
		if reussi:
			somme+=1
			print i

print somme
