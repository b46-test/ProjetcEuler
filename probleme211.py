from numarray import *
from math import sqrt
from euler import premiers

limite=64000000

est_premier=premiers(limite)

sommes=zeros(limite,Int64)

def sigma2(n):
	if n==1:
		sommes[1]=1
		return 1
	if sommes[n]:
		return sommes[n]
	if est_premier[n]:
		total=1+n*n
		sommes[n]=total
		return total
	else:
		k=2
		while n%k or not est_premier[k]:
			k+=1

		additioneur=1
		multiplicateur=0
		cle=n
		while not cle%k:
			cle=cle/k
			additioneur*=k*k
			multiplicateur+=additioneur

		total=(1+multiplicateur)*sommes[cle]
		sommes[n]=total
		return total

compte=0
resume=100000

for i in range(1,limite):
	s=sigma2(i)
	#print s
	if sqrt(s)==int(sqrt(s)):
		compte+=i

	if not i%resume:
		print i,s,compte

print compte
