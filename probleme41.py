def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


def est_premier(n):
	if n[-1]=="5" or not int(n[-1])%2:
		print "bla"
		return False
	i=3
	premier=True
	while i*i<=int(n) and premier:
		if not int(n)%i:
			premier=False
		i+=2
	return premier


max=0
liste="123456789"
for i in range(1,10):
	c=liste[0:i]
	somme=0
	for i in c:
		somme+=int(i)
	if somme%3:
		gen=all_perms(c)
		for i in gen:
			print i
			if est_premier(i):
				if i>max:
					print i
					max=i
	else:
		print c, "ne marche pas"
print max
