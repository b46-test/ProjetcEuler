from sys import setrecursionlimit
setrecursionlimit(100000)
from math import log,sqrt

def cache(f):
	f.cache={}
	def cache_func(*args):
		if args in f.cache:
			return f.cache[args]
		else:
			f.cache[args]=res=f(*args)
			return res
	return cache_func

@cache
def f(n,m):
	if m<1:
		return 0
	if m<2:
		return 1
	if n==1:
		return int(m)
	total=0
	for i in range(1,int(m)+1):
		total+=f(n-1,float(m)/i)
	return total

def produits(deja,puissances,prod,borne):
	assert(len(deja)==len(puissances))
	print "|",deja,puissances,prod,borne
	if deja==[]:
		deja=[2]
		puissances=[1]
		prod=2
	
	d=deja[:]
	pp=puissances[:]
	p=prod

	if p<=borne:
		yield d,pp,p
		pp[len(deja)-1]+=1
		p*=deja[-1]
		for i in produits(d,pp,p,borne):
			yield i

	d[-1]+=1
	pp=puissances[:]

	print "*",prod,deja,puissances
	p=(prod/(deja[-1])**puissances[-1])*d[-1]

	pp[-1]=1
	assert(len(d)==len(pp))
	if p<=borne:
		yield d,pp,p
		for i in produits(d,pp,p,borne):
			yield i
	

	p=prod*(deja[-1]+1)
	d=(deja+[deja[-1]+1])[:]
	pp=(puissances+[1])[:]

	assert(len(d)==len(pp))
	if p<=borne:
		yield d,pp,p
		for i in produits(d,pp,p,borne):
			yield i 

def n(v,p):
	pr=1
	for i in range(len(v)):
		pr*=v[i]**p[i]

	return pr

@cache
def facto(i):
	if i==0 or i==1:
		return 1
	else:
		return facto(i-1)*i

def perm(v,limite):
	p=1
	l=limite
	for i in v:
		for j in range(i):
			p*=l
			l=l-1
		p=p/facto(i)
	return p
	
def vecteurs(deja,puissances,limite):
	assert(len(deja)==len(puissances))

	if n(deja,puissances)<=limite:
		permutations=perm(puissances,limite)
		print deja,puissances

		yield permutations
		p=puissances[:]
		p[-1]+=1
		if n(deja,p)<=limite:
			for i in vecteurs(deja,p,limite):
				yield i
		else:
			p[-1]=1
			d=deja[:]
			d[-1]+=1
			for i in vecteurs(d,p,limite):
				yield i
		
		for i in vecteurs(deja+[deja[-1]+1],puissances+[1],limite):
			yield i

def produits(minimum,longueur,borne):
	if longueur==0 or borne<minimum:
		return 0

	if longueur==1:
		total=0
		for i in range(minimum,int(sqrt(borne))):
			total+=int(log(borne)/log(i))
		total+=borne-sqrt(borne)

		return total

	total=0
	for i in range(minimum,int(sqrt(borne))):
		total+=produits(i+1,longueur-1,float(borne)/i)
	

total=0
limite=10

n=1
p=produits(2,n,limite)
while p>0:
	nb=1
	for i in range(n):
		nb=nb*(limite-n)
		nb=nb/facto(n)

	total+=p/nb
	n+=1
	p=produits(2,n,limite)

print total
