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
def fib(n):
	if n<2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

for i in range(91):
	if i>1:
		print i,fib(i)

