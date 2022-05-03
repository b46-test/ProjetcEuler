max=0
gagnant=0

for n in range(1,1000):
	reste=1
	deja_vus=[]
	sequence=""

	while reste and reste%n not in deja_vus:	
		deja_vus.append(reste)
		reste*=10
		while reste<n:
			reste*=10
			sequence+="0"
			deja_vus.append(0)
		sequence+=str(reste/n)
		reste=reste%n
	
	print sequence
	if reste:
		i=0
		while deja_vus[i]!=reste:
			i+=1
	
		longueur=len(deja_vus)-i
		if longueur>max:
			max=longueur
			gagnant=n
			print gagnant, max

print gagnant
