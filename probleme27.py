from euler import liste_premiers

liste1000=liste_premiers(1000)
liste=liste_premiers(2000)
max=0
produit=0

for b in liste1000:
	for premier in liste:
		a=premier-b-1
		n=2
		while n**2+n*a+b in liste:
			n+=1
		if n>max:
			max=n
			produit=a*b
			a_m=a
			b_m=b

	b=-b
	for premier in liste:
		a=premier-b-1
		n=2
		while n**2+n*a+b in liste:
			n+=1
		if n>max:
			max=n
			print a,b,n
			produit=a*b
			a_m=a
			b_m=b

print max,produit,a_m,b_m

