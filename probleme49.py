from euler import liste_premiers
from euler import chiffres
tableau=liste_premiers(100000);

touches={}

for i in tableau:
    x=chiffres(i)
    if touches.has_key(x):
        touches[x].append(i);
    else:
        touches[x]=[i]
        
for i in touches:
    for s in range(len(touches[i])-2):
        j=touches[i]
        if j[s+1]-j[s]==j[s+2]-j[s+1]:
            print j,s,j[s+2]-j[s+1]
