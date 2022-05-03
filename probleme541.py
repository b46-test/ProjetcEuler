from euler import liste_premiers

def gcd(m,n):
	x, y = max(m, n), min(m, n)
	while x%y != 0:
		x, y = y, x%y
	return y


def decomposition(n):
	i=0
	d={}
	while n>=pr[i]:
		f=0
		while not n%pr[i]:
			f+=1
			n=n/pr[i]
		if f:
			d[pr[i]]=f
		i+=1
	return d

def p(n):
	i=0
	while not n%3:
		n=n/3
		i+=1
	return i

def h(n):
	if n==1:
		return [1,1]
	else:
		a=h(n-1)
		x=a[0]*n+a[1]
		y=a[1]*n
		return[x,y]


pr=liste_premiers(10**6)

print decomposition(10)
print decomposition(120)

n=1
while n<20:
	hn=h(n)
	g=gcd(hn[0],hn[1])
	print h(n),n,decomposition(n),g,decomposition(g),decomposition(hn[0]),decomposition(hn[1])
	n+=1
	
print h(n-1)
