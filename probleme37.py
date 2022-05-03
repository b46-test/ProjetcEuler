premiers=[3,5,7]
trunc=[3,5,7]
def next_truncatable_left(n):
	if n<1:
		yield 0
	elif n==1:
		for i in [2,3,5,7]:
			yield i 
	else:
		gen=next_truncatable_left(n-1)
		for j in gen:
			for i in [1,3,7,9]:
				candidat=10*j+i
				if est_premier(candidat):
					yield candidat

def list_all():
	n=1
	while True:
		gen=next_truncatable_left(n)
		for i in gen:
			yield i
		n+=1

def est_premier(n):
	i=3
	premier=True
	while i*i<=n and premier:
		if not n%i:
			premier=False
		i+=1
	return premier

def est_truncatable_right(n):
	if n==1:
		return False
	reussi=True
	while n>10 and reussi:
		n=int(str(n)[1:])
		if not est_premier(n):
			reussi=False
	return reussi
			
			



gen_trunc=list_all()
total=0
nombre=0
while True:
	i=gen_trunc.next()
	#print i
	if est_truncatable_right(i) and i%10!=1:
		total+=i
		nombre+=1
		print i,total-17,nombre-4

print "fini!"
