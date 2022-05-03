from math import sqrt
#from numarray import zeros
limite=1000
t=[0]*(limite+1)

a=1

max=0

while a<limite:
	b=a
	c=sqrt(a*a+b*b)
	#print a,b,c
	while c+a+b<=limite:
		if c==int(c):
			c=int(c)
			t[a+b+c]+=1
			if t[a+b+c]>max:
				print a+b+c,max
				max=t[a+b+c]
		b+=1
		c=sqrt(a*a+b*b)
	a+=1
