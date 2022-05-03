from euler import liste_premiers
from euler import premiers

maximum=1000000
liste=liste_premiers(maximum)


for i in xrange(21,len(liste),2):
	if sum(liste[0:i])>maximum:
		break
	for k in range(len(liste)-i):
		if(sum(liste[k:k+i]))>maximum:
			break

		if liste.count((sum(liste[k:k+i]))):
			p=sum(liste[k:k+i])
			break
print p
