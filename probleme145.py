def reverse(n):
	total=0
	while n>0:
		total=total*10+n%10
		n=n/10
	return total

def reversible(n):
	if not n%10:
		return False
	t=n+reverse(n)
	r=True
	while t>0:
		if not t%2:
			t=0
			r=False
		else:
			t=t/10
	return r

total=0
for i in xrange(1,1000):
	if reversible(i):
		print i
		total+=1
print total
