borne=50000*1000

primes=[]
a=1
while a*a<borne:
	a+=1
	p=filter(lambda x:a%x==0, filter(lambda x:x*x<=a,primes))
	if not len(p):
		primes+=[a]



carres=[x*x for x in primes]
cubes=filter(lambda x:x<borne,[x*x*x for x in primes])
tetra=filter(lambda x:x<borne,[x*x*x*x for x in primes])

touche={}

for i in tetra:
	for j in filter(lambda x:x+i<borne,cubes):
		for k in filter(lambda x:x+j+i<borne,carres):
			touche[i+j+k]=True

print len(touche)
