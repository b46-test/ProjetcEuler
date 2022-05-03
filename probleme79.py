attempts=["319", "680", "180", "690", "129", "620", "762", "689", "762", "318", "368", "710", "720", "710", "629", "168", "160", "689", "716", "731", "736", "729", "316", "729", "729", "710", "769", "290", "719", "680", "318", "389", "162", "289", "162", "718", "729", "319", "790", "680", "890", "362", "319", "760", "316", "729", "380", "319", "728", "716"]

def passe(x,code):
	j=0
	for i in code:
		if i==x[j]:
			if j==len(x)-1:
				return True
			else:
				j+=1
	return False


def nombres(base,caracteres):
	for i in caracteres:
		if len(caracteres)>1:
			for j in nombres(base+i,map(str,filter(lambda x:x!=i,caracteres))):
				yield j
		else:
			yield base+i

for i in nombres("","12367890"):
	reussi=True
	for j in attempts:
		if not passe(j,i):
			reussi=False
			break
	if reussi:
		print "bravo!",i
		break
