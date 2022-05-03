from itertools import combinations
from euler import liste_premiers
from euler import premiers
from euler import cache

def fonctionne(a,b):
	if(est_premier(int(str(a)+str(b))) and est_premier(int(str(b)+str(a)))):
		return True
	else:
		return False

@cache
def est_premier(n):
	i=0
	while p[i]**2<=n:
		if not n%p[i]:
			return False
		i+=1
	return True

p=liste_premiers(10000)

i=0


while i<len(p):
	print i
	j=i+1
	while(j<len(p)):
		if(fonctionne(p[i],p[j])):
			k=j+1
			while k<len(p):
				if(fonctionne(p[i],p[k]) and fonctionne(p[j],p[k])):
					l=k+1
					while l<len(p):
						if(fonctionne(p[i],p[l]) and fonctionne(p[j],p[l]) and fonctionne(p[k],p[l])):
							m=l+1
							while m<len(p):
								if(fonctionne(p[i],p[m]) and fonctionne(p[j],p[m]) and fonctionne(p[k],p[m]) and fonctionne(p[l],p[m])):
									print p[i]+p[j]+p[k]+p[l]+p[m]
								m+=1
						l+=1
				k+=1
		j+=1
	i+=1
