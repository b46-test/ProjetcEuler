maxi=0
i=10**5
m=10**5
while i>0:
	i-=1
	texte=""
	n=1
	while n*i<m and len(texte+str(n*i))<=9:
		texte+=str(n*i)
		if(len(texte)==9):
			reussi=True
			for j in range(9):
				if(texte.count(str(j+1))!=1):
					reussi=False
					break
			if reussi:
				print i," ",texte
		n+=1
