from euler import liste_premiers
from sys import setrecursionlimit

limite=10**5

p=liste_premiers(limite+100)
n=[0]*len(p)

setrecursionlimit(len(p)*2)

def nombres(actuel,rad,i,n):
	if actuel*p[i]<=limite:
		n[i]=n[i]+1
		if n[i]==1:
			rad*=p[i]
		yield [actuel*p[i],rad]
		for j in nombres(actuel*p[i],rad,i,n):
			yield j

		n[i]-=1
		if n[i]==0:
			rad=rad/p[i]
		for j in nombres(actuel,rad,i+1,n):
			yield j
	
t=[1+limite*10**4]
for i in nombres(1,1,0,n):
	t+=[i[0]+limite*10**4*i[1]]
t.sort()
for i in t:
	print i

print t[10**4-1]
