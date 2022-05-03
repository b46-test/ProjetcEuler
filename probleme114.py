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
def possibilites(nombre):
	if nombre<3:
		return 1
	if nombre==3:
		return 2
	if nombre==4:
		return 4 # rouge+noir, noir+rouge, rouge, noir
	
	total=possibilites(nombre-1)

	for j in range(4,nombre+1):
		total+=possibilites(nombre-j)
	total+=1
	return total

def batons(nombre,base):
#	base=base+"|"
	if nombre<3:
		yield base+nombre*"n"
	elif nombre==3:
		yield base+3*"n"
		yield base+3*"r"
	elif nombre==4:
		yield base+4*"n"
		yield base+4*"r"
		yield base+"n"+3*"r"
		yield base+3*"r"+"n"
	else:
		for j in batons(nombre-1,base+"n"):
			yield j
		for j in range(4,nombre+1):
			for k in batons(nombre-j,base+(j-1)*"r"+"n"):
				yield k
		yield base+nombre*"r"

print possibilites(50)
