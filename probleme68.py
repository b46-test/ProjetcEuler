
def perm(a):
	if(len(a)<=1):
		yield a

	else:
		for i in perm(a[1:]):
			for j in range(len(i)+1):
				yield i[:j] + a[0:1] + i[j:]
		
def affiche(etoile):
	for i in [[0,5,6],[1,6,7],[2,7,8],[3,8,9],[4,9,5]]:
		print [etoile[j] for j in i],sum([etoile[j] for j in i])

	print "\n"

def test_solution(etoile):
	n=sum([etoile[j] for j in [0,5,6]])

	for i in [[1,6,7],[2,7,8],[3,8,9],[4,9,5]]:
		if(sum([etoile[j] for j in i])!=n):
			return False


	return True

print test_solution([10,2,3,4,5,6,7,8,9,1])

for i in perm(xrange(1,10)):
	if test_solution([10]+i):
		affiche([10]+i)
