from math import sqrt
from euler import liste_premiers

limite=1000*1000

p=liste_premiers(limite*2)

def cache(f):
	f.cache={}
	def cache_func(*args):
		if args in f.cache:
			return f.cache[args]
		else:
			f.cache[args]=res=f(*args)
			return res
	return cache_func
def divisors(n):
	yield 1
	i=2
	while i<=sqrt(n):
		if not n%i:
			yield i
			yield n/i
		i+=1
		

@cache
def sum_of_improper_divisors(n,i):
	if n<=2:
		return 1
	else:
		while n%p[i]:
			i+=1
		f=1
		while not n%p[i]:
			n=n/p[i]
			f=f*p[i]+1
		return f*sum_of_improper_divisors(n,i)

def sum_of_divisors(n):
	return sum_of_improper_divisors(n,0)-n



starts=[x for x in xrange(1,limite)]

for i in (12,13,20):
	print sum_of_divisors(i),i,"sum"

i=2
m=0

for n in xrange(2,limite):
	if not n%10000:
		print n
	act=[n]
	
	next_number=sum_of_divisors(n)

	while not next_number in act and next_number<limite and next_number>act[0]:
		act+=[next_number]
		next_number=sum_of_divisors(next_number)
	if next_number in act:
		loop_size=len(act)-act.index(next_number)
		if loop_size>m:
			m=loop_size
			g=act
			print g+[next_number],m,len(g)+1

print g,m
