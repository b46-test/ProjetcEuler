from euler import premiers
import sys

liste=premiers(10**6)
print "j'ai les premiers"
bloub=0

for i in xrange(1,10): 
	for j in range(10):
		for k in range(10):
			if (i+j+k)%3:
				for l in range(6):
					for m in range(l+1,6):
						for n in range(m+1,6):
							reussis=[]
							rates=0
							if not l:
								s=1
							else:
								s=0
							for o in xrange(s,10):
								fixe=[i,j,k]
								w=0
								p=0
								for v in range(6):
									if(v==l or v==m or v==n):
										p=10*p+o
									else:
										p=10*p+fixe[w]
										w+=1
								if liste[p]:
									reussis+=[p]
								else:
									rates+=1
								if len(reussis)==8:
									print reussis
									sys.exit(0)
