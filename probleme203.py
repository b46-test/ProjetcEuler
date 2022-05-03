from math import sqrt
from euler import premiers

def binomial(n,k):
    from euler import facto
    return facto(n)/(facto(n-k)*facto(k))
    
lignes=51

touches={}
for i in range(lignes):
    for j in range(i+1):
        nombre=binomial(i,j)
        #print nombre
        #if not touches.has_key(nombre):
        touches[nombre]=True
    #print

limite=int(sqrt(max(touches)))+1
print "il faut tester ",len(touches)," nombres"


est_premier=premiers(limite)

liste_premiers=[2]
for i in range(3,limite):
    if est_premier[i]:
        liste_premiers.append(i)

print "J'ai les nombres premiers!"

total=0
for i in touches.keys():
    print i
    j=0
    carre=False
    while (not carre) and (j<len(liste_premiers) and liste_premiers[j]**2<=i):
        #print i,liste_premiers[j]
        if not i%(liste_premiers[j]**2):
            #print i,j
            carre=True
        j+=1
        
    
    if not carre:
        total+=i

print
print total