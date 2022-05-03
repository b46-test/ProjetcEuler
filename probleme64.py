from math import sqrt

def developpement(n):
	a=int(sqrt(n))
	c=int(sqrt(n))
	b=1
#	print a,b,c
	
	while True:
		b=(n-c*c)/b
		k=0
		while ((k+1)*b-c)<sqrt(n):
			k+=1
		c=(k*b)-c
	#	print k,b,c
		yield [k,b,c]
MAX=10001
p={}
for n in filter(lambda x:not sqrt(x)==int(sqrt(x)),(x for x in xrange(2,MAX))):
	deja={}
	for i in developpement(n):
		x=",".join(map(str,i))
		if deja.has_key(x):
			break
		else:
			deja[x]=True
	#print n,len(deja)
	p[n]=len(deja)
print len(filter(lambda x:p[x]%2==1,p))
