from numpy import *
from euler import *

maximum=200000

count=0
nb=[0]*maximum	

p=1
while p+1<maximum:
	p+=1
	if nb[p]==0:
		count=0
		i=p
		while i<maximum:
			nb[i]+=1
			i+=p
	elif nb[p]==4:
		count+=1
		if count==4:
			print p-3
			break
	else:
		count=0
