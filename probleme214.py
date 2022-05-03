from numarray import zeros
from math import sqrt
limite=36000

def gcd(i,j):
    a=min(i,j)
    b=max(i,j)
    
    if not b%a:
        return a
    else:
        for c in range(int(sqrt(b)),0,-1):
            if not a%c and not b%c:
                return c

def phi(n):
    total=0
    for i in range(1,n):
        if gcd(i,n)==1:
            total+=1
    return total

resultats=zeros(limite+1)
def longueur(n):
    if n==1:
        return 1
    if resultats[n]:
        return resultats[n]
    else:
        l=longueur(phi(n))+1
        resultats[n]=l
        return l
    
resume=1000
for i in range(1,limite):
    l=longueur(i)
    if l>=25 or not i%resume:
        print i,longueur(i)
        