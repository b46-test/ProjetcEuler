def f(x):
	return int(2**(30.403243784-x*x))/(10.0**9)

u=-1

nombres={}

n=0
boucle=False

while boucle==False:
	n+=1
	u=f(u)
	for i in nombres:
		if nombres[i]==u:
			print i,n
			boucle=True
	nombres[n]=u

for i in range(10):
	u=f(u)
	print u

print u+f(u)
