def u(n):
	#return n**3
	return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

def op(k,n):
	f=0
	for i in xrange(1,k+1):
		p=u(i)
		for j in xrange(1,k+1):
			if j!=i:
				p=p*float(j-n)/(j-i)
		f+=p
	return f

total=0
for k in xrange(1,11):
	n=1
	while u(n)==op(k,n):
		n+=1
	total+=op(k,n)	

print total
