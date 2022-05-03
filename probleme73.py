from euler import liste_premiers

MAX=10**4+2*10**3
print MAX

print "Calcul des nombres premiers"
p=liste_premiers(MAX)

n=[0]*len(p)
actuel=1
total=0

def nombres(actuel,phi,n,i,borne,p):
	total=phi
	#print actuel,phi,total
	while i+1<len(p) and p[i+1]*actuel<=borne:
		i+=1
		n[i]+=1
		if n[i]==1:
			f=p[i]-1
		else:
			f=p[i]
		for w in nombres(p[i]*actuel,f*phi,n,i-1,borne,p):
			yield w
		n[i]-=1
	yield actuel

print "Calcul des fractions"	
for i in nombres(1,1,n,-1,MAX,p):
	p2=filter(lambda x:i%x,p)
	borne=i/2+1
	for j in nombres(1,1,n,-1,borne,p2):
		if i<3*j and 2*j<i:
			#print j,i
			total+=1
			if not total%10000:
				print total

print total
