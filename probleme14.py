from numarray import zeros

# nouveau dictionaire qui stocke toutes les longueurs
# deja calculees
resultats={}


def longueur(n):
    
    if not resultats.has_key(n):
        if n==1:
            resultats[n]=1
        elif n%2:
            resultats[n]=1+longueur(3*n+1)
        else:
            resultats[n]=1+longueur(n/2)
    
    return resultats[n]
maximum=0
for i in range(1,1000000):
    candidat_maximum=longueur(i)
    #print i,candidat_maximum
    if candidat_maximum>maximum:
        gagnant=i
        maximum=candidat_maximum
        
        print gagnant
        print maximum
