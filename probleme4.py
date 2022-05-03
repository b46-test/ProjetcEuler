

# teste si un nombre est un palindrome ou non
def is_palindrome(nombre):
    texte=str(nombre)
    tests=len(texte)/2
    for i in range(tests):
        #print str(i)+":"+texte[i]+texte[-i-1]
        if texte[i]!=texte[-i-1]:
            return False
    
    return True
    
gagnant=0

for i in range(999,99,-1):
    for j in range(i,gagnant/i,-1):
        candidat=i*j
        if is_palindrome(candidat):
            print str(i)+"*"+str(j)+"="+str(candidat)
            if candidat>gagnant:
                gagnant=candidat

print gagnant