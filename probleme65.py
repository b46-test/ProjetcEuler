def denom(n):
	if n==0:
		return 2
	
	if not (n+1)%3:
		return 2*(n+1)/3
	else:
		return 1

n=99
a=denom(n)
b=1
while n>0:
	n=n-1
	tmp=a
	a=denom(n)*a+b
	b=tmp
print a,b
print sum(map(int,list(str(a))))
