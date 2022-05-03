from math import sqrt

def successive_square_sum(cur,i,limit):
	cur+=[i]
	#print cur
	if sum(map(lambda x:x*x,cur))<limit:
		if len(cur)>=2:
			yield sum(map(lambda x:x*x,cur))
		for i in successive_square_sum(cur,i+1,limit):
			yield i


def is_palindrome(i):
	return str(i)==str(i)[::-1]

total=0
n=[]

print is_palindrome(595)

MAX=10**8
for j in range(1,int(sqrt(MAX)+1)):
	for i in successive_square_sum([],j,MAX):
		if is_palindrome(i):
			print i
			n+=[i]

print sum(set(n))
