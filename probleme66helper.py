from math import sqrt

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
def a(n,D):
	if n==0:
		return int(sqrt(D))
	else:
		return int(sqrt((a(0,D)+P(n,D))/Q(n,D)))
@cache
def p(n,D):
	if n==0:
		return a(0,D)
	elif n==1:
		return a(0,D)*a(1,D)+1
	else:
		return a(n,D)*p(n-1,D)+p(n-2,D)

@cache
def q(n,D):
	if n==0:
		return 1
	elif n==1:
		return a(1,D)
	else:
		return a(n,D)*q(n-1,D)+q(n-2,D)

@cache
def P(n,D):
	if n==0:
		return 0
	elif n==1:
		return a(0,D)
	else:
		return a(n-1,D)*Q(n-1,D)-P(n-1,D)

@cache
def Q(n,D):
	if n==0:
		return 1
	elif n==1:
		return D-a(0,D)*a(0,D)
	else:
		return (D-P(n,D)*P(n,D))/Q(n-1,D)

m=0

for j in range(1,1000):
	if sqrt(j)==int(sqrt(j)):
		print j,"est carre"
		continue
	D=j
	i=0
	while(p(i,D)*p(i,D)-q(i,D)*q(i,D)*D!=1):
		i+=1
#	print D,p(i,D),q(i,D),p(i,D)*p(i,D)-q(i,D)*q(i,D)*D
	if(p(i,D)>m):
		m=p(i,D)
		mD=D
		print m,mD
print m,mD
