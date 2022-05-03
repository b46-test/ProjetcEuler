# The cube, 41063625 (345^(3)), can be permuted to 
# produce two other cubes: 56623104 (384^(3)) and 
# 66430125 (405^(3)). In fact, 41063625 is the 
# smallest cube which has exactly three 
# permutations of  its digits which are also cube.

# Find the smallest cube for which exactly five 
# permutations of its digits are cube.

from numpy import sort

def chiffres(nombre):
	return "".join(sort(list(str(nombre))))

nombre={}

for i in range(10,50000):
    cube=i**3
    
    cle=chiffres(cube)
    
    if nombre.has_key(cle):
        nombre[cle].append(i)
    else:
        nombre[cle]=[i]

gagnant=10000000000000
for i in nombre.keys():
    if len(nombre[i])==5:
        print i,nombre[i]
        candidat=min(nombre[i])
        if candidat<gagnant:
            gagnant=candidat
print gagnant,gagnant**3
