zones=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
bulls=[25]


print 21+62*21+62*63*21/2


singles=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25]
doubles=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 50]
trebles=[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]

target=singles+doubles+trebles

total=0

for i in doubles:
	total+=1

for i in range(len(target)):
	for j in doubles:
		if target[i]+j<100:
			total+=1

for i in range(len(target)):
	for j in xrange	(i,len(target)):
		for k in doubles:
			if target[i]+target[j]+k<100:
				total+=1

print total
		
	


