def permutations(a):
	if len(a)==1:
		yield a
	elif len(a)>0:
		for i in permutations(a[1:]):
			for j in range(len(i)+1):
				yield i[:j]+[a[0]]+i[j:]


def targets(a):
	if len(a)==1:
		yield a[0]
	elif len(a)>0:
		for h in permutations(a):
			for i in range(len(h)):
				for j in targets(h[:i]):
					for k in targets(h[i:]):
						yield float(j)/k
						if j>k:
							yield j-k
						yield j*k
						yield j+k

def atteints(a):
	n=0
	s=set()
	for i in targets(a):
		if int(i)==i:
			s.add(int(i))

	s=sorted(s)
	return s

def score(s):
	return max(filter(lambda x:s[x]==x+1,range(len(s)))+[0])+1
	
v=0
limite=10
mini=1
for i in xrange(mini,limite):
	for j in xrange(i+1,limite):
		for k in xrange(j+1,limite):
			for l in xrange(k+1,limite):
				s=atteints([i,j,k,l])
				t=score(s)
				if t>v:
					v=t
					print i,j,k,l,t,s
