from euler import somme_des_chiffres


gagnant=0
for a in range(1,100):
    for b in range(1,100):
        candidat=somme_des_chiffres(a**b)
        if candidat>gagnant:
            gagnant=candidat
            print a,b,gagnant