a=[x for x in xrange(1,11)]

def sous_ensembles(tab):
	for d1 in range(len(tab)-5):
		for d2 in xrange(d1+1,len(tab)-4):
			for d3 in xrange(d2+1,len(tab)-3):
				for d4 in xrange(d3+1,len(tab)-2):
					for d5 in xrange(d4+1,len(tab)-1):
						for d6 in xrange(d5+1,len(tab)):
							yield [d1,d2,d3,d4,d5,d6]

def test(d1,d2,n):
	return (n[0] in d1 and n[1] in d2) or (n[1] in d1 and n[0] in d2)

nb=0
failed=False

print "vrai",test([1,2,3,4],[5,6,7,8],[8,4])
print "vrai",test([1,2,3,4],[5,6,7,8],[4,8])
print "faux",test([1,2,3,4],[5,6,7,8],[4,9])

for premier in sous_ensembles([1,2,3,4,5,6,7,8,9,0]):
	if (6 in premier) or (9 in premier):
		premier+=[6,9]
	for deuxieme in sous_ensembles([1,2,3,4,5,6,7,8,9,0]):
		if (6 in deuxieme) or (9 in deuxieme):
			deuxieme+=[6,9]
		for i in [[0,1],[0,4],[0,6],[1,6],[2,5],[3,6],[4,6],[6,4],[8,1]]:
			if not test(premier,deuxieme,i):
				failed=True
		if not failed:
			nb+=1
		failed=False

print nb,nb/2
