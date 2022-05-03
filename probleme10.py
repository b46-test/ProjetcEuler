# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from math import sqrt
from numarray import *

cible=2000000

# entree: nombre
# sortie: liste des premiers inferieurs au nombre donne
def premiers(nombre):
    premier=ones(nombre)

    for j in range(4,nombre,2):
        premier[j-1]=0
    
    i=3
    while i*i<nombre:
        
        if(premier[i-1]):
            #print i
            for j in range(i*i,nombre+1,2*i):
                premier[j-1]=0
        
        i=i+2
    
    return premier


somme=0

liste=premiers(cible)
for i in range(1,cible):
    if liste[i]:
        somme=somme+i+1

print somme