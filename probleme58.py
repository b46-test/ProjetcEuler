from euler import liste_premiers
pr=liste_premiers(1000000)


def est_premier(n):
	i=0
	while pr[i]*pr[i]<=n:
		if not n%pr[i]:
			return False
		i+=1
	return True


n=[0,0,0,0]
d=[0,0,0,0]
n[0]=3
d[0]=10

n[1]=5
d[1]=12

n[2]=7
d[2]=14

n[3]=9
d[3]=16


p=3
r=1
while float(p)/(4*r+1)>0.1:
	for i in range(4):
		n[i]+=d[i]
		if est_premier(n[i])==1:
			print n[i],"premier"
			p+=1
		else:
			print n[i],"pas premier"
		d[i]+=8
	r+=1
	print r,p,float(p)/(4*r+1)
print r*2+1
