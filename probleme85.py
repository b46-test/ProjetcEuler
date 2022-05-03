
# b=4000000/(n*n+n)


# m = (-1 + sqrt(1+4b))/2



from math import sqrt

but=2000000
meilleur=0
mn=0
mm=0
diff=but

print but

def rectangles(a,b):
	return (a*a+a)*(b*b+b)/4

def hauteur(largeur, but):
	B=4*but/(largeur*largeur+largeur)
	return (-1+sqrt(1+4*B))/2

for n in range(but):
	if n>0:
		m=int(hauteur(n,but))
		r0=rectangles(n,m)
		r1=rectangles(n,m+1)
	#	print n,m,r0,r1
		assert(r0<=but and r1>=but)

		if r0==0:
			break

		if abs(but-r0)<diff:
			diff=abs(but-r0)
			meilleur=m*n
			mm=m
			mn=n
			print meilleur,diff,mn,mm,"*",rectangles(mn,mm)
		if abs(but-r1)<diff:
			diff=abs(but-r1)
			meilleur=(m+1)*n
			mm=m+1
			mn=n
			print meilleur,diff,mn,mm,"*",rectangles(mn,mm)
	
print meilleur,diff,but-rectangles(mn,mm),mn,mm
