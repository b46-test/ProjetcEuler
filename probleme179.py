from euler import premiers

# limite=10**7 pour le probleme "officiel"

limite=10**7
resume=10000

def nombre_de_diviseurs(n):
    from math import sqrt
    if n==1:
        return 1
    
    if est_premier[n]:
        return 2
    
    i=0
    total=1
    nombre=0
    while n>1:
        if est_premier[n]:
            return 2*total
        #print n," est pas premier"
        while not n%liste_premiers[i]:
            n=n/liste_premiers[i]
            nombre+=1
        #print liste_premiers[i],nombre
        total*=nombre+1
        nombre=0
        i+=1
        
    return total

est_premier=premiers(limite)

liste_premiers=[2]
for i in range(3,limite):
    if est_premier[i]:
        liste_premiers.append(i)
        
#print liste_premiers
print "J'ai tous les premiers inferieurs a ",limite
ancien=0
paires=0
for i in range(2,limite):
    if not est_premier[i]:
        nb=nombre_de_diviseurs(i)
        if nb==ancien:
            paires+=1
        #print i,nb
        ancien=nb
    else:
        ancien=0
    
    if not i%resume:
        print i,paires
        
print paires
#for i in range(10**7):
	#total=nombre_de_diviseurs(i)
	#if total==ancien_total:
##		print nombre,i,total
		#nombre+=1
	#ancien_total=total
	#if not i%10000:
		#print i
#print nombre
