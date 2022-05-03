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
def fact(n):
	if n>1:
		return n*fact(n-1)
	else:
		return 1

@cache
def suivant(n):
	return sum([fact(i) for i in map(int,str(n))])

def ordonnes(n):
	r=0
	t=map(int,str(n))
	t.sort()
	d=10**(len(t)-1)
	for i in t:
		if i==0:
			i=1
		r+=d*i
		d/=10

	return r	


longueurs={}


i=0
while i<10**6:
	i+=1
	n=i

	if not n in longueurs:
		if not n%10**4:
			print n
		if ordonnes(n) in longueurs:
			longueurs[n]=longueurs[ordonnes(n)]
		elif suivant(n)==n:
			longueurs[n]=1
			longueurs[ordonnes(n)]=1

		else:
			dejavus=[n]
			while suivant(n) not in dejavus:
				n=suivant(n)
				dejavus+=[n]
	
			r=suivant(n)
		
			for k in range(dejavus.index(r)):
				longueurs[dejavus[k]]=len(dejavus)-k
				longueurs[ordonnes(dejavus[k])]=len(dejavus)-k
			
			for k in xrange(dejavus.index(r),len(dejavus)):
				longueurs[dejavus[k]]=len(dejavus)-dejavus.index(r)
				longueurs[ordonnes(dejavus[k])]=len(dejavus)-dejavus.index(r)
total=0
for i in longueurs:
	if longueurs[i]==60:
		print i
		total+=1

print total
