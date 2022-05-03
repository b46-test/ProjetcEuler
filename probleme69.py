from math import sqrt


def pgdc(i,j):
	a=min(i,j)
	while a>0:
		if not i%a and not j%a:
			return a
		a-=1

gagnant=0
ngagnant=0
	
MAX=100000
premiers=range(2,MAX+1)
i=0


while i*i<premiers[-1]:
	premiers=filter(lambda x:x<=premiers[i]*(premiers[i]-1) or x%premiers[i],premiers)
	i=i+1

limite=0
premiers_utiles=[2]

for i in xrange(2,MAX):
	if premiers_utiles[-1]<i:
		limite+=1
		if limite<len(premiers):
			premiers_utiles=premiers_utiles+[premiers[limite]]
	nombres=xrange(1,i+1)
	facteurs=filter(lambda x:not i%x,premiers_utiles)
	phi=i
	for j in facteurs:
		phi=(phi*(j-1))/j


	v=i/float(phi)
#	if not i%1000 or i<10:
#		print i,facteurs,phi,v,ngagnant,gagnant

	if(v>gagnant):
		gagnant=v
		ngagnant=i
		print "***",ngagnant,v

print ngagnant,gagnant
