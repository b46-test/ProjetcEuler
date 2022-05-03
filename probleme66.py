from math import sqrt

l=1000
for D in range(l):
	if(sqrt(D)==int(sqrt(D))):
		continue
	r=0
	y=1
	x=0
	while x*x-D*y*y!=1:
		y=y+1
		x=int(sqrt(1+D*y*y))
	
	print x,y,D,x*x-D*y*y
