digits=[1,2,3,4,3,2]



def suivant(x):
	return (x*10**6+4232097)%123454321

k=0
total=0
totaux={}
for i in xrange(1,100000):
	t=0
	d=0
	while t<i:
		t+=digits[k%6]
		d=d*10+digits[k%6]
		k+=1
	total=(total+d)%123454321
	if totaux.has_key(total):
		l=t
		print "**",l
	else:
		totaux[total]=k
	if not i%1000:
		print i,t,str(d)[-3:],total

print l

atteints={}

k=0
total=0

x=suivant(suivant(suivant(260521232097)))
n=0

while not atteints.has_key(x):
	atteints[x]=n
	n+=1
	x=suivant(x)

print x,n,atteints[x]
a=260521232097
for i in range(55556):
	a=suivant(a)
print a

	
