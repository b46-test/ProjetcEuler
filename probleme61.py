from math import sqrt

def polygonal(n):
	r=[]
	if int((-1.0+sqrt(1+8*n))/2)==(-1.0+sqrt(1+8*n))/2:
		r+=[0]
	if sqrt(n)==int(sqrt(n)):
		r+=[1]
	if int((1.0+sqrt(1+24*n))/6)==(1.0+sqrt(1+24*n))/6:
		r+=[2]
	if int((1.0+sqrt(1+8*n))/4)==(1.0+sqrt(1+8*n))/4:
		r+=[3]
	if int((3.0+sqrt(9+40*n))/10)==(3.0+sqrt(9+40*n))/10:
		r+=[4]
	if int((2.0+sqrt(4+12*n))/6)==(2.0+sqrt(4+12*n))/6:
		r+=[5]
	return r

def fonctionne(t):
	if t.count([]):
		return False
	for i in range(6):
		if t.count([i])>1:
			return False
	
	for i in range(6):
		for j in range(6):
			if t.count([i,j])>2:
				return False
			if t.count([i,j])==2 and (t.count([i]) or t.count([j])):
				return False

	d=[]
	for i in t:
		if len(i)==1 and d.count(i[0]):
			return False
		elif len(i)==1:
			d+=[i[0]]
		else:
			reussi=False
			for j in i:
				if not d.count(j):
					reussi=True
			if not reussi:
				return False
	return True


for n in range(20):
	for i in xrange(10,100):
		print i
		for j in xrange(i,100):
			p0=polygonal(100*i+j)
			if(fonctionne([p0])):
				for k in xrange(10,100):
					p1=polygonal(100*j+k)
					if fonctionne([p1,p0]):
						for l in xrange(10,100):
							p2=polygonal(100*k+l)
							if fonctionne([p2,p1,p0]):
								for m in xrange(10,100):
									p3=polygonal(100*l+m)
									if fonctionne([p3,p2,p1,p0]):
										for n in xrange(10,100):
											p4=polygonal(100*m+n)
											p5=polygonal(100*n+i)
											if fonctionne([p5,p4,p3,p2,p1,p0]):
												print 100*i+j,100*j+k,100*k+l,100*l+m,100*m+n,100*n+i
												print 101*i+101*j+101*k+101*l+101*m+101*n
												for o in [p0,p1,p2,p3,p4,p5]:
													print o
