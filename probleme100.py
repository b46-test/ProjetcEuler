from math import sqrt
from euler import liste_premiers

p=liste_premiers(10**5)

def isqrt(n):
    xn = 1
    xn1 = (xn + n/xn)/2
    while abs(xn1 - xn) > 1:
        xn = xn1
        xn1 = (xn + n/xn)/2
    while xn1*xn1 > n:
        xn1 -= 1
    return xn1

def factors(n,i=0):
	r=[]
	if n==1:
		return []
	while n%p[i]:
		i+=1
	while (not n%p[i]) and n>0:
		n=n/p[i]
		r+=[p[i]]
	return factors(n,i)+r




i=2
j=2

pi=1
pj=1

print factors(4)

while True:
	lhs=i*(i-1)
	rhs=2*j*(j-1)
	if(lhs==rhs):
		print i,j,"*",factors(i),factors(i-1),factors(j),factors(j-1)
		i+=1
	elif (lhs>rhs):
		j+=1
	else:
		i+=1


#while True:
#	if not k%1000000:
#		print k
#	r=1+8*(k*k-k)
#	d=int(sqrt(r))
#	if d*d==r:
#		n=(1+d)/2
#		print k,n,(n*n-n)-2*(k*k-k)
#	k+=1
