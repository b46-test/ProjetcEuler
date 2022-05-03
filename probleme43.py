from itertools import *

def prop(n):
	if int(n[1:4])%2:
		return False
	if int(n[2:5])%3:
		return False
	if int(n[3:6])%5:
		return False
	if int(n[4:7])%7:
		return False
	if int(n[5:8])%11:
		return False
	if int(n[6:9])%13:
		return False
	if int(n[7:10])%17:
		return False
	
	return True

total=0
for i in permutations(["1","2","3","4","5","6","7","8","9","0"]):
	if prop("".join(i)):
		n=int("".join(i))
		total+=n
		print n,total
