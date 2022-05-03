from euler import puissance_imprecise




#1777^^1855

base=1777
exposant=2
precision=10

resultat=base

for i in range(exposant):
    resultat=(base**resultat)%(10**precision)
    print i,resultat
    
print resultat