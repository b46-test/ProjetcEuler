def cache(f):
	f.cache={}
	def cache_func(*args):
		if args in f.cache:
			return f.cache[args]
		else:
			f.cache[args]=res=f(*args)
			return res
	return cache_func

@cache
def est_abondant(n):
	return n<sum([x for x in range(1,n) if not n%x])

abondants=[12]
total=0

for i in range(28123):
	reussi=False
	if i>abondants[0]:
		for j in abondants:
			if est_abondant(i-j):
				reussi=True
		if abondants[len(abondants)-1]<i/2+5:
			for k in range(abondants[len(abondants)-1]+1,i/2+5):
				if est_abondant(k):
					abondants.append(k)
					if est_abondant(i-k):
						reussi=True
	if not reussi:
		total+=i
		print i,total

print total
