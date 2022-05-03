from euler import liste_premiers
from operator import mul
from sys import setrecursionlimit

limite=10**6

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

def nombre(vecteur):
	n=1
	for i in range(len(vecteur)):
		n*=premiers[i]**vecteur[i]
	return n

def nb_fractions(vecteur):
	p=1	
	for i in vecteur:
		p*=2*i+1
	return (p+1)/2

but=4*10**8
def essais(v):
	if nb_fractions(v)<=but:
		for i in essais(v+[1]):
			yield i
		if (len(v)<2 or v[-2]>v[-1]) and nombre(v)<=MIN:
			v[-1]+=1
			for i in essais(v):
				yield i
	else:
		yield v

v=[1]

MIN=10**100
for i in essais(v):
	if nombre(i)<MIN:
		MIN=nombre(i)
		print nombre(i),i

