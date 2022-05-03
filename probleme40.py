def digit():
	i=0
	while True:
		i+=1
		for j in str(i):
			yield int(j)

gen=digit()
p=1
d=1
for i in range(1,1000001):
	c=gen.next()
	if i==d:
		p*=c
		print d,i,c
		d*=10
print p
