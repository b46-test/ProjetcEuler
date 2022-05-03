from math import sqrt

phi=(1-sqrt(5))/2
PHI=(1+sqrt(5))/2

def fibo():
	n=1
	t=0
	i=0
	while True:
		i+=1
		t+=n
		n=t-n
		t=t%(10**10)
		n=n%(10**10)
		yield t

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
def f(k):
	if k<4:
		return int(( PHI**k - phi**k )/sqrt(5))
	elif k%2:
		n=(k+1)/2
		return f(n-1)**2+f(n)**2
	else:
		n=k/2
		return (2*f(n-1)+f(n))*f(n)


# (Public) Returns F(n).
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (int(str(c)[0:1000]), int(str(d)[0:1000]))
		else:
			return (int(str(d)[0:1000]), int(str(c + d)[0:1000]))


def pandig(s):
	if(len(set(filter(lambda x:int(x)>0,s)))==9):
		return True
	else:
		return False

def matrix_mult(a, b):
    return ((a[0][0]*b[0][0] + a[0][1]*b[1][0], 
             a[0][0]*b[0][1] + a[0][1]*b[1][1]),
            (a[1][0]*b[0][0] + a[1][1]*b[1][0], 
             a[1][0]*b[0][1] + a[1][1]*b[1][1]))


def matrix_pow(a, k):
    if k == 0:
        return ((1, 0), (0, 1))
    t = matrix_pow(a, k//2)
    t2 = matrix_mult(t, t)
    if k % 2 == 0:
        return t2
    return matrix_mult(t2, a)


def fib(n):
    a = ((1, 1), (1, 0))
    return matrix_pow(a, n)[0][1]


def get_first_k(n, k):
    return str(fib(n))[:k]


state=[0,1]

def next_fibo():
	global state
	prev=0
	n=1

	while True:
		state=map(lambda x:x%(10**9),[state[1],state[0]+state[1]])

		return state[1]

for i in range(2,1000000):
	f=next_fibo()
	if(pandig(str(f))):
		print i,f
		if(pandig(str(get_first_k(i,9)))):
			print i,"est la solution"
			print fib(i)
			break
