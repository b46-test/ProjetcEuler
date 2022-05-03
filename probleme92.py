from numarray import zeros

liste_fins=zeros(10**7)

def fin(i):
    if i==89 or i==1:
        return i
    
    if liste_fins[i]:
        #print i," je suis deja passe par la..."
        return liste_fins[i]
    else:
        truc=fin(next(i))
        liste_fins[i]=truc
        return truc

def next(i):
    total=0
    while i>0:
        total+=(i%10)**2
        i=i/10
    
    return total

resume=10**6
nombre=0
for i in range(1,10**7):
    if fin(i)==89:
        nombre+=1
    
    if not i%resume:
        print i,nombre

print "Total: ",nombre
#i=149293949
#liste
#nombre=0
#for i in range(1,10**7):
    #truc=i
    ##print i
    #while not (truc==1 or truc==89):
        ##print truc
        #truc=next(truc)
        #if liste_1.has_key(i):
            #truc=1
        #else if liste_89.has_key(i):
            #truc=89
            
    #if truc==89:
        #nombre+=1
        
#print nombre