primes=[]
def cache(f):
	f.cache={}
	def cache_func(*args):
		if args in f.cache:
			return f.cache[args]
		else:
			f.cache[args]=res=f(*args)
			return res
	return cache_func

def pop_primes(n):
    global primes
    l=[1]*n
    i=1
    while i*i<=n:
        i+=1
        if l[i]:
            for j in range((n-1)/i-1):
                l[2*i+j*i]=0

    for i in xrange(2,n):
        if l[i]:
            primes+=[i]

@cache
def dec(n):
    p=[]
    i=0
    while(primes[i]**2<=n):
        if not n%primes[i]:
            p=[primes[i]]+dec(n/primes[i])
            p.sort()
            return p
        i+=1

    return [n]

pop_primes(10**4)
print dec(10)
print dec(97)
print dec(700)
t=0
for i in xrange(1,10**7):
    d=dec(4*i+1)
    t=(t+d[-1])%(10**18)
    if not i%10000:
        print(i,d[-1],t)

print t
