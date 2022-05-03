from math import sqrt

l=10**9



def gcd(m,n):
	x, y = max(m, n), min(m, n)
	while x%y != 0:
		x, y = y, x%y
	return y

total=0

for n in xrange(1,int(sqrt(l))):
	for k in [-1,1]:
		m=sqrt(3*n*n+k)
		if(int(m)==m):
			a=m*m-n*n
			b=2*m*n
			c=m*m+n*n

			p=2*a+2*c
			
			if(p<=l):
				total+=p
				print 2*a,c,p,total
#n=1
#m=4



	d=sqrt(12*n*n+4)
	m=(4*n+d)/2
	if(int(m)==m):
		a=m*m-n*n
		b=2*m*n
		c=m*m+n*n

		p=2*b+2*c
		
		if(p<=l):
			total+=p
			print "*",2*b,c,p,total

	m=(4*n-d)/2
	if(int(m)==m and m>n):
		a=m*m-n*n
		b=2*m*n
		c=m*m+n*n

		p=2*b+2*c
		
		if(p<=l):
			total+=p
			print "**",2*b,c,p,total
