# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can 
# see that the 6th prime is 13.

# What is the 10001st prime number?


from math import sqrt

cible=10001

# entree: liste des n premiers premiers
# sortie: le premier suivant
def prochain_premier(liste):
    retour=-1
    candidat=liste[-1]
    
    
    while retour==-1:
        i=0
        possible=True
        candidat=candidat+1
    
        while liste[i]<=sqrt(candidat) and possible and i<len(liste):
            if candidat%liste[i]==0:
                possible=False
            i=i+1
            
        if possible:
            retour=candidat
        
        
    return retour




liste=[2];

while len(liste)<cible:
    liste.append(prochain_premier(liste))
    print str(liste[-1])+"->"+str(len(liste))
