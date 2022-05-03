from numarray import ones
limite=10**8

premiers=[2]
est_premier=ones(limite/2)

n=3
total=1
maxi=0
w=0
while n<limite/2:
	while n<limite/2 and not est_premier[n]:
		n+=2
	
	i=n*n
	while i<limite/2:
		est_premier[i]=False
		i+=2*n

	premiers.append(n)
	if(n*n<limite):
		maxi=len(premiers)-1
		total+=len(premiers)
	else:
		while maxi>-1 and premiers[maxi]*n>limite:
			maxi-=1
		total+=maxi+1
	n+=2
	w+=1
	if not w%1000 or w<10:
		print n

print total
