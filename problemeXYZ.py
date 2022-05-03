carres=[]

limite=2*10**9

i=0
ic=i*i
while ic<limite:
	i+=1
	ic=i*i
	j=i
	jc=ic+j*j
	while jc<=limite:
		carres.append(jc)
		j+=1
		jc=ic+j*j
	if not i%10:
		print i,j
