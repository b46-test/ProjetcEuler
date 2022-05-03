from math import sqrt
from euler import premiers
from euler import liste_premiers

m=100000000

def divisors(n):
	i=1
	while i<=sqrt(n):
		if not n%i:
			yield i
			yield n/i
		i+=1
		

p=premiers(m)
lp=liste_premiers(m)

n=1
total=0
for x in lp:
	n=x-1
	rate=False
	for d in divisors(n):
		if not p[d+n/d]:
			#print n,d
			rate=True
			break

	if not rate:
		total+=n
	if not n%10000:
		print n

print total
