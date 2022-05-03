from euler import liste_premiers

MAX=10**6

print "Calcul des nombres premiers"
p=liste_premiers(MAX)

n=[0]*len(p)
actuel=1
total=0

def nombres(actuel,phi,n,i):
	total=phi
	#print actuel,phi,total
	while i+1<len(p) and p[i+1]*actuel<=MAX:
		i+=1
		n[i]+=1
		if n[i]==1:
			f=p[i]-1
		else:
			f=p[i]
		total+=nombres(p[i]*actuel,f*phi,n,i-1)
		n[i]-=1
	return total

print "Calcul des fractions"	
print nombres(1,1,n,-1)-1
