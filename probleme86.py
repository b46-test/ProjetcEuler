from math import sqrt


def carre(x):
	return int(sqrt(x))==sqrt(x)

def longueur(a,b,c):
	return sqrt(c*c+(a+b)*(a+b))


M=1817
cuboids=0

for a in xrange(1,M+1):
	if not a%1000:
		print a
	for bc in xrange(1,2*a+1):
		l=a*a+bc*bc
		if carre(l):
			b=max(1,bc-a)
			while b<=a and bc-b>=b:
				c=bc-b
		#		print a,b,c,"=",l
				cuboids+=1
				b+=1


print cuboids
