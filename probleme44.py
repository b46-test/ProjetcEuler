from euler import cache
from math import sqrt

def p(n):
	return n*(3*n-1)/2

@cache
def est_penta(n):
	x=(0.5+sqrt(0.25+6*n))/3
	return x==int(x)

i=0
fini=False
while not fini:
	i+=1
	d=p(i)
	k=1
	while (2*d-3*k*k+k)>0:
		if not (2*d-3*k*k+k)%(6*k):
			n=(2*d-3*k*k+k)/(6*k)
			if(est_penta(p(n)+p(n+k))):
				print d,n,k,est_penta(p(n+k)-p(n))
				fini=True
		k+=1
