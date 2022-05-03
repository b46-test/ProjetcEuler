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
def facto(n):
	print "calcul pour ", n
	return n*facto(n-1) if n>0 else 1
