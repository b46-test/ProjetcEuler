MAX=100


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
def asc(i,l):
	if l==1:
		return 10-i

	if i==9:
		return 1

	total=0
	for j in range(i,10):
		total+=asc(j,l-1)
	return total

@cache	
def desc(i,l):
	if l==1:
		return i+1

	if i==0:
		return 1

	total=0
	for j in range(0,i+1):
		total+=desc(j,l-1)
	return total

a=asc(0,MAX)
b=0
for i in range(MAX):
	b+=desc(9,MAX-i)

print a+b-MAX*10-1
