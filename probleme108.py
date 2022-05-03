from euler import liste_premiers
from operator import mul
from sys import setrecursionlimit

limite=10**7

setrecursionlimit(limite)

premiers=liste_premiers(limite+1)

def cache(f):
	f.cache={}
	def cache_func(*args):
		if args in f.cache:
			return f.cache[args]
		else:
			f.cache[args]=res=f(*args)
			return res
	return cache_func

def fractions(n):
	p=1
	for i in facteurs(n):
		p*=2*i+1
	return (p+1)/2

@cache
def facteurs(n):
	f=0
	i=0
	if n==1:
		r=[]
	while i<len(premiers) and n%premiers[i]:
		i+=1
	if i<len(premiers):
		while not n%premiers[i]:
			f+=1
			n=n/premiers[i]
		r=[f]
		r+=facteurs(n)
	return r

MAX=0
for i in range(10**5,10**7):
	f=fractions(i)
	if f>MAX:
		print i,f
		MAX=f
