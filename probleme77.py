from euler import liste_premiers
from sys import setrecursionlimit
setrecursionlimit(3000)

limite=5000000000000000000000

premiers=liste_premiers(3000)

mem={}

def solutions(n,m):
    #print n,m
    if m<0 or n<0:
        return 0
    
    cle=str(n)+"*"+str(m)
    if mem.has_key(cle):
        return mem[cle]
    
    if m==0:
        if n%2:
            return 0
        else:
            return 1
    mem[cle]=solutions(n-premiers[m],m)+solutions(n,m-1)
    return mem[cle]

#print solutions(10,13)


possibilites=0
i=5



while possibilites<limite:
    i=i+1
    possibilites=solutions(i,len(premiers)-1)
print i,possibilites
    
    