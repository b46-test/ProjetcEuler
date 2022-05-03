#coding=UTF-8
from math import sqrt


limite=1500000
total=0
touche={}

def gcd(m,n):
	x, y = max(m, n), min(m, n)
	while x%y != 0:
		x, y = y, x%y
	return y

print gcd(1,3)
print gcd(4,8)
print gcd(36,27)

for m in xrange(1,int(sqrt(limite)/2)):
	for n in xrange(m+1,int(sqrt(limite-(m*m)))+1):
		#print m,n
		if(gcd(m,n)==1 and m%2!=n%2):
			x=n*n-m*m
			y=2*m*n
			z=m*m+n*n
		
			l=x+y+z	
			d=1
			while(d*l<=limite):
				if touche.has_key(d*l):
					#print m,n,d*x,d*y,d*z,d*l
					touche[d*l]+=1
					if touche[d*l]==2:
						total-=1
				else:
					#print m,n,d*x,d*y,d*z,d*l
					touche[d*l]=1
					total+=1
				d+=1
			if l>limite:
				continue
print total
print 12,touche[12]
print 120,touche[120]
print 48,touche[48]

print len(filter(lambda x:touche[x]==1,touche))

