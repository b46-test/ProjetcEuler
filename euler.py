# entree: nombre
# sortie: liste des premiers inferieurs au nombre donne
def premiers(nombre):
    print "Calcul des premiers jusqu'a",nombre,"..."
    from numpy import ones
    premier=ones(nombre)
    
    premier[0]=0
    premier[1]=0

    for j in range(4,nombre,2):
        premier[j]=0
    
    i=3
    while i*i<nombre:
        
        if(premier[i]):
            #print i
            for j in range(i*i,nombre,2*i):
                premier[j]=0
        
        i=i+2

    print "ok\n"
    
    return premier
            
def liste_premiers(nombre):
    print "Calcul des premiers jusqu'a",nombre,"..."
    liste=[2]
    from numpy import ones
    premier=ones(nombre)
    
    premier[0]=0
    premier[1]=0

    for j in range(4,nombre,2):
        premier[j]=0
    
    i=3
    while i<nombre:
        
        if(premier[i]):
            liste.append(i)
            #print i
            for j in range(i*i,nombre,2*i):
                premier[j]=0
        
        i=i+2
    
    print "ok\n"
    return liste

def somme_des_chiffres(n):
    total=0
    while n>0:
        total=total+n%10
        n=n/10
        
    return total
    
    
def facto(n):
    if n==1 or n==0:
        return 1
    else:
        return n*facto(n-1)
    
    
def nombre_de_chiffres(n):
    total=1
    while n>=10:
        n=n/10
        total+=1
    return total
    
def somme_des_diviseurs(n):
    from math import sqrt
    i=2
    total=1
    racine=sqrt(n)
    while i<racine:
        if not n%i:
            total+=n/i+i
        i+=1
    
    if racine==int(racine):
        total+=int(racine)
    
    return total
    
# teste si un nombre est un palindrome ou non
def is_palindrome(nombre):
    texte=str(nombre)
    tests=len(texte)/2
    for i in range(tests):
        #print str(i)+":"+texte[i]+texte[-i-1]
        if texte[i]!=texte[-i-1]:
            return False
    
    return True
    

def hyperexpo(a,b):
    if b==1:
        return a
    else:
        return a**hyperexpo(a,b-1)

def puissance_imprecise(base,exposant,precision):
    return (base**exposant)%(10**precision)


def somme_imprecise(a,b,precision):
    return (a+b)%(10**precision)

def chiffres(nombre):
    from numpy import sort
    if nombre==0:
        return 0
    else:
        tableau=[]
        while nombre>0:
            tableau.append(nombre%10)
            nombre=nombre/10
        
        tableau=sort(tableau)
        #print tableau
        
        exp=1
        
        retour=0
        for i in tableau:
            retour+=i*exp
            exp*=10
            
        return retour


def cache(f):
	f.cache={}
	def cache_func(*args):
		if args in f.cache:
			return f.cache[args]
		else:
			f.cache[args]=res=f(*args)
			return res
	return cache_func
