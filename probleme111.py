import gmpy
from euler import liste_premiers
from euler import premiers
from math import sqrt


taille=10

premiers=liste_premiers(int(sqrt(10**taille))+10)


def nombres(t,d,i,base):
#	print t,d,i,base
	if base==0:
		length=0
	else:
		length=len(str(base))
	assert(i<=t-length)

	if base and length+i==t:
		yield base*10**i+int(i*str(d))
	elif i==0:
		for j in range(10**(t-length)):
			if not str(d) in str(j):
				yield base*10**(t-length)+j
	else:
		if base or d:
			for j in nombres(t,d,i-1,base*10+d):
				yield j
		if length<t-1:
			for j in filter(lambda x:x!=d,range(10)):
				if base*10+j:
					for k in nombres(t,d,i,base*10+j):
						yield k
	
	

def ms(t,d):
	for z in range(1,t-1):
		i=t-z
		s=0
		for j in nombres(t,d,i,0):
			k=0
			while premiers[k]<=sqrt(j) and j%premiers[k]:
				k+=1
			if j%premiers[k]:
				s+=j
		
		if s>0:
			return i,s
total=0
for i in range(10):
	m=ms(10,i)
	print i,m
	total+=m[1]

print total

