from numpy import ones
from operator import mul
limite=6


def sommes(n,k,m):
	if k==1 and m<=n:
		yield [n]
	else:
		for i in range(m,n-k+2):
			for j in sommes(n-i,k-1,i):
				yield [i]+j

def products(n,m):
	if n==1:
		yield []
	else:
		for i in range(m,n+1):
			if not n%i:
				for j in products(n/i,i):
					yield [i]+j
		
		

longueurs=set(range(2,12001))

n=3

g=set()

while len(longueurs):
	n+=1
	for p in products(n,2):
		k=reduce(mul,p)-sum(p)+len(p)
		if k in longueurs:
			print k,n
			longueurs.remove(k)
			g=g.union(set([n]))

print sum(g)
