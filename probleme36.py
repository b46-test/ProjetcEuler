from sys import setrecursionlimit

setrecursionlimit(30000)

def palindromes(n):
	if n<1:
		yield ""
	elif n==1:
		for i in range(10):
			yield str(i)
	elif n==2:
		for i in range(10):
			if i==0:
				yield "00"
			else:
				yield str(i+10*i)
	
	else:
		for i in range(10):
			for j in palindromes(n-2):
				yield str(i)+j+str(i)
def est_pal_bin(n):
	#print candidat
	bin=""
	while n!=0:
		bin+=str(n%2)
		n=n/2
	for i in range(len(bin)/2+1):
		if bin[i]!=bin[-i-1]:
			return False
	return True

somme=0

for i in [1,3,5,7,9]:
	if est_pal_bin(i):
		somme+=i

for i in range(5):
	for j in palindromes(i):
		for k in ["1","3","5","7","9"]:
			candidat=int(k+j+k)
			if est_pal_bin(candidat):
				somme+=candidat

print somme
