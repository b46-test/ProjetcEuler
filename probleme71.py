m=10**6


but=[3,7]

#a/b<c/d

#a*d<c*b

#x*7<3*k
#3*k/7-1

gagnant=[0,1]
for i in range(0,m+1):
	if not i==but[1]:
		x=(but[0]*i)/but[1]
		if(x*gagnant[1]>i*gagnant[0]and but[0]*i>but[1]*x):
			gagnant=[x,i]

print gagnant

