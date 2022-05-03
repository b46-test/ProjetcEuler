for i in range(1,10):
	for j in range(i+1,10):
		facteur=2
		while i*facteur<100 and j*facteur<100:
			if facteur%10:
				dessus=i*facteur
				dessous=j*facteur
				if dessus/10==i:
					if(dessus%10==dessous/10 and dessous%10==j) or (dessus%10==dessous%10 and dessous/10==j):
						print i,j,dessus,dessous
				
				if dessus%10==i:
					if(dessus/10==dessous/10 and dessous%10==j) or (dessus/10==dessous%10 and dessous/10==j):
						print i,j,dessus,dessous
			facteur+=1
