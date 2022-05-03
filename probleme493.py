from numpy import ones
import random
from math import factorial

urn=range(70)

total=0
n=0

def repartitions(a,s):
	if len(a)<9:
		for i in xrange(0,min(11,21-s)):
			for x in repartitions(a+[i],i+s):
				yield x
	else:
		if s>9:
			yield a+[20-s]

def comb(k,n):
	return factorial(n)/(factorial(n-k)*factorial(k))
	

for i in repartitions([],0):
	n=1
	d=len(filter(lambda x:x>0,i))
	for j in i:
		n=n*comb(j,10)
	print n, d, i 
	total+=d*n
	print total
print total
