def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

tableau=[]
for p in all_perms("123456789"):
	for i in range(1,3):
		if int(p[0:i])*int(p[i:5])==int(p[5:9]):
			print int(p[0:i])," ",int(p[i:5])," ",int(p[5:9]) 
			tableau.append(p[5:9])

print sum([int(i) for i in set(tableau)])
