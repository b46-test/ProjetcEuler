from euler import cache

@cache
def est_premier(n):
	i=2
	while i*i<=n:
		if not n%i:
			return False
		i+=1
	return True

n=27
reussi=True
while reussi:
	n+=2
	if not est_premier(n):
		reussi=False
		c=1
		while 2*c*c<=n-2:
			if est_premier(n-2*c*c):
				reussi=True
				break
			c+=1
		if not reussi:
			print n,"xx"
