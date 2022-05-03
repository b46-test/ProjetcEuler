from euler import liste_premiers
from math import sqrt
from random import randrange

limit=10**14

p=liste_premiers(int(sqrt(limit))+5)

def digits_sum(n):
	total=0
	while n>0:
		total+=n%10
		n=n/10
	return total

def miller_rabin(n, k=20):
	if n == 2:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in xrange(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in xrange(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True

def is_prime(n):
	return miller_rabin(n)
	i=0
	while n%p[i] and p[i]<=sqrt(n):
		i+=1

	if not n%p[i]:
		return False
	return True

harshad=[1,2,3,4,5,6,7,8,9]
strong=[18]

old=harshad
total=0


for k in range(14):
	new=[]
	for i in old:
		for j in range(10):
			h=10*i+j
			n=digits_sum(h)
			if h<limit:
				if not h%n:
					new+=[h]
					
					if h/n==2 or h/n==3 or (h>3 and is_prime(h/n)):
						strong+=[h]

				if is_prime(h) and i in strong:
					print "srth",h
					total+=h
	harshad+=new
	old=new

print total
