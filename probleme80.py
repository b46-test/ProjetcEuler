import gmpy
from math import sqrt

gmpy.set_minprec(400)


t=gmpy.mpf(5)


total=0

for i in range(100):
	if sqrt(float(i))!=int(sqrt(float(i))):
		t=str(gmpy.mpf(i).sqrt())
		ptotal=int(t[0])
		for j in range(2,101):
			ptotal+=int(t[j])
		total+=ptotal
		print i,ptotal,total
print total
