from euler import cache
from euler import nombre_de_chiffres

@cache
def f(n):
	if n==0:
		return [1,1]
	else:
		[d,v]=f(n-1)
		return [2*v+d,v+d]

total=0
tableau=xrange(1,1001)
print len(filter(lambda x:nombre_de_chiffres(f(x)[0])>nombre_de_chiffres(f(x)[1]),tableau))
