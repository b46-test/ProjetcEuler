from euler import cache

@cache
def c(n,k):
	if k>n/2:
		return c(n,n-k)
	if k==0:
		return 1
	elif n==0:
		return 0
	else:
		return c(n-1,k-1)+c(n-1,k)

nombre=0
for i in range(101):
	for r in range(i+1):
		if c(i,r)>10**6:
			nombre+=1
		print c(i,r)

print nombre
